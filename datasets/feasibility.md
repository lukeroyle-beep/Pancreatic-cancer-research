# A measured limit on pancreatic organoid validation

**Decision, 27 November 2026.** Hold confirmatory testing of the association between CDP-diacylglycerol synthase 1 (CDS1) expression and CDS2 knockout fitness in donor-independent pancreatic ductal adenocarcinoma (PDAC) organoids using these two atlases. Both rarity of eligible material and prior publication change the scientific question. This is a metadata audit and a lookup of already published statistics.

| What was counted | Verified finding | Interpretation |
|---|---:|---|
| Neiswender and colleagues, all next-generation models with the published paralog test | CDS2 fitness versus CDS1 expression, Pearson correlation 0.62636, nominal two-sided probability 2.79 × 10⁻¹⁷, 146 models. Traditional-model correlation 0.58412. | The biomarker and its association in next-generation models are prior art. The cohort spans lineages and model types. This is an author-reported association. |
| Same deposit, second endpoint | CDS2 fitness versus the PDAC-classical expression programme, correlation −0.03023, nominal probability 0.7562, 108 organoids | Different predictor, mixed-lineage organoids. A small correlation here does not refute the CDS1 association. The programme name does not describe the cohort. |
| Broad paper metadata, pancreatic adenocarcinoma code PAAD, screen quality passed, expression available | 23 dome-culture three-dimensional screens in 23 models. 60 traditional two-dimensional screens in 44 models. | Model counts precede donor deduplication, histology adjudication and gene-level completeness. Repeated screens can inflate the denominator. |
| Sanger supplement, primary tumour listed as pancreatic | 22 models with expression. Four have both expression and knockout screening, from four distinct donors. All four are marked as having no Broad overlap. | Eighteen expression-only models cannot validate knockout effects. The source's overlap flag is an initial screen for independence. |
| Morphology of the four Sanger donors | One infiltrating duct carcinoma (8500/3), three adenocarcinoma unspecified (8140/3) | At most four under an inclusive pancreatic-adenocarcinoma rule, one explicitly ductal under a strict rule. Excluding unspecified histology should be decided without viewing effects. |
| Small-sample check | Under four independent exchangeable donors, no rank ties, a two-sided exact Spearman permutation test has minimum attainable probability 2/4! = 1/12. | Even a perfect ranking cannot meet a conventional two-sided 0.05 test. This is a property of the design. A negative replication or absence of biology cannot be inferred. |

The two screened sources separately tested their models. The Broad-wide paralog estimate was already exposed in prior work. An independent biological confirmation needs sufficiently many separately derived, measured PDAC models. Pancreatic cell lines can test technical agreement and lend context. Tumour expression and predicted dependency cannot supply the missing knockout outcomes. No individual response was analysed here.

**Reproduction.** Run from the repository root with Python 3.12.14. The checker reads four public files, verifies their byte hashes, prints only aggregates and fetches into a directory you specify. The largest input is the public Sanger supplementary archive, about 127 MB. Use a temporary cache outside the repository. The receipts are deterministic and use no randomness.

```sh
python3.12 -m venv /tmp/pcr-evidence-venv
/tmp/pcr-evidence-venv/bin/pip install openpyxl==3.1.5 et-xmlfile==2.0.0
/tmp/pcr-evidence-venv/bin/python datasets/check_organoid_evidence.py /tmp/pcr-organoid-metadata --download > /tmp/pcr-evidence.json
diff -u datasets/organoid-feasibility.json /tmp/pcr-evidence.json
```

**Provenance.** Neiswender and colleagues supply the screen and published result tables in version 1 of their Figshare deposit. The archive README defines both correlation cohorts. The Sanger donor counts use only Supplementary Table 2, sheets `data_availability` and `clinical_data`, linked by model ID. Individual-level and screen-level records remain with the sources. The receipt reproduces two published gene-level summary associations, attributed to Neiswender and colleagues under the Figshare deposit’s Creative Commons Attribution 4.0 terms. The [checker](check_organoid_evidence.py) records file identifiers, locations and SHA-256 (Secure Hash Algorithm 256-bit) digests. The [aggregate receipt](organoid-feasibility.json) preserves precise author values. Independent checking in this audit also examined the Sanger table separately and recovered the same four-donor ceiling. [Broad v1](https://doi.org/10.6084/m9.figshare.29472362.v1) · [Sanger article and supplement](https://doi.org/10.1038/s41586-026-10830-y) · [Prior transportability study, section 2.7](https://doi.org/10.3390/biology15191782).

**Limits.** No estimate of a PDAC-only CDS1/CDS2 effect, patient response or therapeutic index follows. Additional archives may exist. Before reopening the question, identify a measured new cohort, document full donor and dataset relationships, genotype and histology, freeze the endpoint and smallest informative effect and justify achievable interval width.
