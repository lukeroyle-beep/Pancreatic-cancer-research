# Historical phase III trial report screen

**225 article records were screened.** On 27 November 2026, an unthemed search for pancreatic cancer in titles or abstracts, restricted to the indexed phase III clinical trial publication type, retrieved 225 PubMed records and 223 Europe PMC (Europe PubMed Central) records. All 223 Europe PMC records also appeared in PubMed. Each of the two additional PubMed articles is a trial companion report. The search extends to all indexed dates from 1 January 1900. The two queries differ in publication date semantics. Exact queries, per-index hashes, retrieval time and article identifiers accompany this report. [Queries](queries.tsv) · [Membership](membership.tsv) · [Screen](screen.tsv)

## Screening decisions

One evidence analyst screened every title and consulted abstracts for ambiguous population, publication type, endpoint or primary-versus-companion status. Three reports lacked a PubMed abstract and were assigned provisional commentary exclusions from their titles (identifiers 21050812, 27757498 and 27490715). Treatment reports required comparative antitumour or multimodal treatment results in pancreatic cancer or a separable pancreatic subgroup. For older articles describing pancreatic carcinoma, confirm eligibility and histology in the full text before extracting outcomes. Companion reports included secondary analyses, target biomarker studies, adverse effects, quality of life and repeat analyses of treatment trial participants. Uncontrolled studies, cross-trial pools or unclear provenance receive a separate disposition. Screening decisions and family names are preliminary until independent full-text adjudication.

| Report-level disposition | Count |
|---|---:|
| Comparative pancreatic treatment results | 88 |
| Trial-associated reports, including follow-ups and secondary analyses | 94 |
| Context or design requiring adjudication | 8 |
| Design or protocol without clinical results | 12 |
| Wrong population or histology | 8 |
| Diagnosis or detection | 5 |
| Commentary or clinical overview | 5 |
| Supportive care without a pancreatic antitumour comparison | 3 |
| Health economic model | 2 |
| Total | 225 |

The counts represent publications. The same participants can appear in different reports, and a single article can span multiple trials. The screen flags recognizable trial families and indexed registry identifiers. A blank family field means unresolved linkage. Before any pooling, compare intervention, eligibility, sites, recruitment dates, numbers randomised and registration identifiers across all reports. Even the two distinct articles [16767907](https://pubmed.ncbi.nlm.nih.gov/16767907/) and [15700852](https://pubmed.ncbi.nlm.nih.gov/15700852/) report the same arms, survival estimates and sample allocation. They cannot be treated as independent replications.

## Findings that affect research design

| Clinical observation | Implication for a computational claim |
|---|---|
| The November 2026 daNIS-2 trial randomised 490 patients after a separate safety run-in. Adding the transforming growth factor beta antibody NIS793 to nab-paclitaxel and gemcitabine produced median overall survival of 9.2 versus 11.2 months. The hazard ratio was 1.26 (95% confidence interval 1.01–1.59). The trial stopped early after an unfavourable benefit–risk assessment, despite a pharmacodynamic signal of target engagement. | A stromal signature or target-engagement biomarker can point in a misleading direction for clinical outcomes. Any expression-defined subgroup in this trial needs prospective confirmation. [Report](https://doi.org/10.1016/j.esmoop.2026.108621) · [Registry](https://clinicaltrials.gov/study/NCT04935359) |
| In AVATAR, 125 patients were randomised to conventional management or a sequencing and experimental-model strategy. Only 16 of the 81 assigned to the latter had experimental models generated. Of 39 who received second-line treatment in that arm, four received a matched treatment. Median overall survival was 8.7 versus 8.6 months in the assigned groups. | Report feasibility for **all eligible patients**. The four who reached matched treatment were selected after randomisation. Their outcomes cannot establish a benefit of the strategy. [Trial report](https://doi.org/10.1158/1078-0432.CCR-23-4026) |
| Among 154 randomised platinum-responsive or stable patients with metastatic pancreatic cancer and germline BRCA1/2 (breast cancer susceptibility gene 1 or 2) mutations, POLO found median progression-free survival of 7.4 versus 3.8 months with maintenance olaparib versus placebo. The hazard ratio was 0.53 (95% confidence interval 0.35–0.82). Final median overall survival was 19.0 versus 19.2 months, hazard ratio 0.83 (0.56–1.22). | This is a molecularly selected clinical comparator for synthetic lethality. Specify the population and endpoint. The follow-up and initial report use the same cohort. [Primary analysis](https://pubmed.ncbi.nlm.nih.gov/31157963/) · [Final overall survival](https://pubmed.ncbi.nlm.nih.gov/35834777/) |
| Expression of human equilibrative nucleoside transporter 1 was associated with outcome in gemcitabine-treated resected tumours in RTOG 9704 (Radiation Therapy Oncology Group trial 9704). Two later randomised-trial tissue analyses using the SP120 antibody did not confirm predictive value. They include an advanced-disease study and an adjuvant study. | This is a concrete example of the importance of assay, scoring, specimen selection and disease-setting harmonisation. A within-arm survival association alone does not estimate interaction with treatment. [Initial study](https://doi.org/10.1053/j.gastro.2008.09.067) · [Advanced setting](https://doi.org/10.1016/j.ejca.2014.04.023) · [Adjuvant setting](https://doi.org/10.1016/j.ejca.2015.05.005) |
| In hyaluronan-high metastatic pancreatic adenocarcinoma, HALO-109-301 showed a higher response rate after adding pegvorhyaluronidase alfa (47% versus 36%) and nearly identical median overall survival (11.2 versus 11.5 months, hazard ratio 1.00, 95% confidence interval 0.80–1.27). | Objective response and overall survival can diverge in biomarker-selected populations. An organoid or image response cannot establish survival benefit. [Trial report](https://pubmed.ncbi.nlm.nih.gov/32706635/) |

## Coverage and verification

The disease vocabulary and indexing filter miss real trials. A concrete false negative is the 1997 trial of first-line gemcitabine versus fluorouracil, whose title uses “pancreas cancer”. Its PubMed identifier 9196156 is absent from the retrieved membership. Data on trial registration, completed studies with no publication, unindexed phase classifications, and reports without the four pancreatic terms require complementary searches. The phase III tag also retrieves commentaries, protocols and non-PDAC (pancreatic ductal adenocarcinoma) populations. The selected contrasts demonstrate concrete design constraints. They do not estimate an aggregate treatment effect. [Missed landmark](https://pubmed.ncbi.nlm.nih.gov/9196156/) · [Clinical evidence overview](https://www.cancer.gov/types/pancreatic/hp/pancreatic-treatment-pdq)

Reproduce the identifier export from the repository root with Python 3.12 (standard library). The destination must be new or empty.

```sh
python3 literature/search/phase3/retrieve_trials.py --output /tmp/pcr-phase3-new
python3 literature/search/phase3/verify_trials.py
```

The dates in the screening ledger are Europe PMC's indexed first-publication dates; a first-of-month convention can reflect partial historical date precision. The two-index query returned PubMed identifiers for every hit, and PubMed metadata and Europe PMC article records were retrieved for all 225. SHA-256 (Secure Hash Algorithm 256-bit) digests apply to sorted source identifiers with a final newline. Live re-runs may differ after retrospective indexing. Full-text duplicate screening, trial-family reconciliation, comparison extraction, risk-of-bias assessment by independent reviewers and a registry-based coverage expansion remain outstanding.
