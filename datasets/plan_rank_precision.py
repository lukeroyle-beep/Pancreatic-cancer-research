"""Design simulation only. No biological or validation response data are inputs."""

import json

import numpy as np
from scipy.stats import rankdata


SEED = 20261127
SIMULATIONS = 40000


def rank_correlations(generator, donors, population_spearman):
    # Continuous Gaussian copula, so the population Spearman correlation is known.
    pearson = 2 * np.sin(np.pi * population_spearman / 6)
    samples = []
    for _ in range(SIMULATIONS // 2000):
        x = generator.standard_normal((2000, donors))
        noise = generator.standard_normal((2000, donors))
        y = pearson * x + np.sqrt(1 - pearson**2) * noise
        squared_rank_distance = ((rankdata(x, axis=1) - rankdata(y, axis=1)) ** 2).sum(axis=1)
        samples.append(1 - 6 * squared_rank_distance / (donors * (donors**2 - 1)))
    return np.concatenate(samples)


def main():
    rows = []
    for donors in [20, 30, 38]:
        null = rank_correlations(np.random.default_rng([SEED, donors, 0]), donors, 0)
        critical = np.quantile(np.abs(null), 0.95, method="higher")
        for i, effect in enumerate([0, 0.3, 0.5], 1):
            estimates = rank_correlations(np.random.default_rng([SEED, donors, i]), donors, effect)
            rejection = float((np.abs(estimates) > critical).mean())
            rows.append({
                "donors": donors, "assumed_spearman": effect,
                "simulated_estimate_2.5_and_97.5_percentiles": np.quantile(estimates, [0.025, 0.975]).round(4).tolist(),
                "empirical_two_sided_rejection_probability": round(rejection, 4),
                "monte_carlo_standard_error_given_threshold": round((rejection * (1 - rejection) / SIMULATIONS) ** 0.5, 4),
                "critical_absolute_rho_strictly_exceeded": round(float(critical), 6),
            })
    print(json.dumps({"seed": SEED, "draws_per_scenario": SIMULATIONS, "scenarios": rows}, indent=2))


if __name__ == "__main__":
    main()
