import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def load_and_prepare_data(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path)

    df = df[["loan_amount", "interest_rate", "grade", "sub_grade", "loan_status"]]
    df = df.dropna(subset=["loan_amount", "interest_rate", "grade", "loan_status"])

    df["loan_amount"] = pd.to_numeric(df["loan_amount"], errors="coerce")
    df["interest_rate"] = pd.to_numeric(df["interest_rate"], errors="coerce")
    df = df.dropna(subset=["loan_amount", "interest_rate"])

    pd_map = {
        "A": 0.01,
        "B": 0.02,
        "C": 0.04,
        "D": 0.07,
        "E": 0.12,
        "F": 0.20,
        "G": 0.30
    }

    df["PD"] = df["grade"].map(pd_map)
    df = df.dropna(subset=["PD"])

    np.random.seed(42)
    df["LGD"] = np.random.uniform(0.4, 0.6, len(df))
    df["EAD"] = df["loan_amount"]
    df["LOSS_IF_DEFAULT"] = df["EAD"] * df["LGD"]

    return df


def monte_carlo_losses(PD: np.ndarray, loss_if_default: np.ndarray, n_scenarios: int) -> np.ndarray:
    n_loans = len(PD)
    losses = np.zeros(n_scenarios)

    for s in range(n_scenarios):
        random_numbers = np.random.rand(n_loans)
        defaults = (random_numbers < PD).astype(int)
        losses[s] = np.sum(defaults * loss_if_default)

    return losses


def calculate_risk_metrics(losses: np.ndarray) -> dict:
    VaR_95 = np.percentile(losses, 95)
    VaR_99 = np.percentile(losses, 99)

    ES_95 = losses[losses >= VaR_95].mean()
    ES_99 = losses[losses >= VaR_99].mean()

    return {
        "Mean Loss": losses.mean(),
        "VaR 95%": VaR_95,
        "VaR 99%": VaR_99,
        "ES 95%": ES_95,
        "ES 99%": ES_99,
        "Worst Case Loss": losses.max()
    }


def plot_distribution(losses: np.ndarray, VaR_95: float, VaR_99: float, output_path: str):
    plt.hist(losses, bins=50)
    plt.axvline(VaR_95, linestyle="--", label=f"VaR 95% = {VaR_95:,.0f}")
    plt.axvline(VaR_99, linestyle="--", label=f"VaR 99% = {VaR_99:,.0f}")

    plt.title("Monte Carlo Credit Portfolio Loss Distribution")
    plt.xlabel("Portfolio Loss")
    plt.ylabel("Frequency")
    plt.legend()

    plt.savefig(output_path, dpi=300)
    plt.close()


def run_simulation(file_path: str, n_scenarios: int = 10000, stress_multiplier: float = 1.5):
    df = load_and_prepare_data(file_path)

    PD = df["PD"].values
    loss_if_default = df["LOSS_IF_DEFAULT"].values

    # Base simulation
    losses = monte_carlo_losses(PD, loss_if_default, n_scenarios)
    metrics = calculate_risk_metrics(losses)

    # Stress simulation
    PD_stress = np.minimum(PD * stress_multiplier, 1.0)
    losses_stress = monte_carlo_losses(PD_stress, loss_if_default, n_scenarios)
    metrics_stress = calculate_risk_metrics(losses_stress)

    # Save metrics
    summary = pd.DataFrame({
        "Metric": list(metrics.keys()),
        "Base Scenario": list(metrics.values()),
        "Stress Scenario": list(metrics_stress.values())
    })

    summary.to_csv("outputs/risk_summary.csv", index=False)

    # Plot
    plot_distribution(
        losses,
        metrics["VaR 95%"],
        metrics["VaR 99%"],
        "outputs/loss_distribution.png"
    )

    print("Simulation completed.")
    print(summary)
