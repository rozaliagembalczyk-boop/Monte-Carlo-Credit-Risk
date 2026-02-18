from src.monte_carlo_simulator import run_simulation

if __name__ == "__main__":
    run_simulation(
        file_path="data/loan_data.csv",
        n_scenarios=10000,
        stress_multiplier=1.5
    )
