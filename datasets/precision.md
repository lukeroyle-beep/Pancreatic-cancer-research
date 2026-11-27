# What could 38 organoid donors resolve?

A planning calculation for the proposed frozen gemcitabine score, dated 27 November 2026. **No observations or validation response values were used.** The [input audit](pharmacotyping.md) identified 38 eligible organoids each recorded as one sample per patient. The calculation asks what that many genuinely independent, completely observed donors can resolve under favourable assumptions.

| Assumed true Spearman correlation | 95% range of estimates over simulated studies with 38 donors | Probability of rejecting zero in a two-sided 5% test |
|---|---|---:|
| 0.00 | −0.318 to 0.320 | 4.87% |
| 0.30 | −0.022 to 0.571 | 44.31% |
| 0.50 | 0.211 to 0.716 | 89.54% |

The central 95% is a **sampling range given the stated effect**, not an interval for a measured biological effect. Donors were simulated independently with untied continuous measurements from a Gaussian copula. For a chosen population Spearman correlation s, the underlying Gaussian correlation is 2 sin(πs/6). Each scenario used 40,000 paired datasets. A separate 40,000-dataset null simulated the 95th percentile of absolute sample correlations; an independent zero-effect scenario checked its size. The Monte Carlo standard errors at 38 donors, conditional on the finite null cutoff, are 0.11, 0.25 and 0.15 percentage points in table order. Measurement error, tied or censored responses, donor relatedness, missing predictors and range restriction can change performance. The full [receipt](rank-planning.json) includes 20- and 30-donor sensitivity cases.

A development question which requires reliable detection or exclusion of a correlation around 0.30 needs a larger or more informative external cohort. If the agreed objective is to challenge a large effect, the available cohort could support a useful test once score portability and independence are verified. The intended effect size is a scientific choice for prespecification. A 0.05 decision by itself would answer less than an estimate and a donor-level uncertainty interval.

Run the [planning script](plan_rank_precision.py) in Python 3.12.14 with NumPy 2.3.5 and SciPy 1.17.0. It uses seed 20261127 with separate streams per sample size and effect. For independent verification, compare a separate simulation or permutation-based calculation; Monte Carlo estimates need not match to the fourth decimal.

```sh
python3.12 -m venv /tmp/pcr-rank-env
/tmp/pcr-rank-env/bin/pip install numpy==2.3.5 scipy==1.17.0
/tmp/pcr-rank-env/bin/python datasets/plan_rank_precision.py > /tmp/pcr-rank-plan.json
diff -u datasets/rank-planning.json /tmp/pcr-rank-plan.json
```
