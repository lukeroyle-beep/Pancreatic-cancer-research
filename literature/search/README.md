# PCR-001 bibliographic searches and screened records

**As of 27 November 2026**, the seven treatment-related queries retrieved 19,138 distinct source identifiers. Four overlapping screens assigned decisions to **453 distinct source identifiers**. Their individual sizes were 100 for the amended paralogue search, 29 for November surveillance, 116 for historical reviews and themed phase III reports, and 225 for the disease-only phase III search. The 16 themed phase III articles recur in the disease-only search and one review recurs in the November search. Multiple reports can still describe one study. Four mixed-cancer reviews await full-text eligibility adjudication, and eight phase III-indexed reports need design or provenance checks. The wider seven-theme corpus is a searchable queue. It has not been dual-screened or synthesised in its entirety. This release supports a systematic evidence map with a bounded novelty audit. It cannot establish an exhaustive systematic review of all pancreatic cancer treatments.

## What was counted

Queries ran directly on PubMed Entrez and Europe PubMed Central (Europe PMC) application programming interfaces. The exports contain source identifiers for every match. Sources overlap extensively. “Common” counts the same identifier appearing in both indexes. Some publications have two different identifiers, most conspicuously PubMed identifiers for preprints versus Europe PMC preprint identifiers. Topic totals also overlap. Query counts do not measure evidence strength.

| Arm | PubMed | Europe PMC | Common identifiers | Union |
|---|---:|---:|---:|---:|
| Genetic dependencies and synthetic lethality | 482 | 517 | 432 | 567 |
| KRAS (Kirsten rat sarcoma viral oncogene homolog) | 4,826 | 4,970 | 4,526 | 5,270 |
| Treatment resistance | 3,896 | 3,801 | 3,491 | 4,206 |
| Microenvironment and immune evasion | 6,907 | 6,898 | 6,225 | 7,580 |
| Repurposing and combinations | 3,762 | 3,821 | 3,526 | 4,057 |
| RNA (ribonucleic acid) therapeutics | 1,760 | 1,791 | 1,699 | 1,852 |
| Computational discovery | 161 | 172 | 145 | 188 |
| Seven themes combined | 17,608 | 17,920 | 16,390 | 19,138 |
| Preprint update, 1 January 2025–27 November 2026 | 147 | 475 | 0 | 622 |
| Focused novelty, first query | 6 | 5 | 5 | 6 |
| Focused novelty, sensitivity amendment | 73 | 93 | 66 | 100 |
| All ten arms combined | 17,680 | 18,012 | 16,455 | 19,237 |

Exact translated strings, result counts and hashes are in the [main query log](census/queries.tsv) and [November query log](november/queries.tsv). Machine-readable [main](census/membership.tsv.gz) and [November](november/membership.tsv.gz) exports contain database and arm memberships. [Eligibility and field semantics](criteria.md) specify the populations, exclusions and amendment. One reviewer conducted each bounded screen. A second researcher still needs to adjudicate eligibility and risk of bias.

## Focused novelty findings

Of the 100 returned identifiers, three are journal articles presenting directly relevant original evidence, 16 additional records provide mechanistic or computational context, five represent versions or duplicate index entries, and 76 were excluded. The register gives each decision, screening basis, identifier and related version. It exposes false positives such as the yeast checkpoint kinase sharing the Cds1 name and false negatives in the first query. Nonretrieval of an exact regression specification is weak evidence of originality. [Focus screen](focus-screen.tsv)

1. Guo et al. already connected cytidine diphosphate diacylglycerol synthase 2 (CDS2) dependency with mesenchymal state in pancreatic ductal adenocarcinoma (PDAC). The authors used Cancer Dependency Map (DepMap) 24Q2 and studied multiple clinical and preclinical sources. A new scan reproducing that signal adds no priority claim. [Guo et al., 21 August 2025](https://doi.org/10.1016/j.celrep.2025.116191)
2. Arnoldus et al. used combined Broad and Sanger dependency data, including 21Q2 and 23Q4 analyses, and tested the CDS1/CDS2 interaction in cancer models. Replicate releases can share cell models and screen inputs. [Arnoldus et al., 4 July 2025](https://doi.org/10.1038/s41588-025-02221-2)
3. Chan et al. analysed Project Score and Project Achilles separately. Their methods specify institute-specific expression sources, the threshold of one on the log2(transcripts per million + 1) scale, and a two-sided test comparing essentiality between high and low expressers. Their experimental work included uveal melanoma. Even a second-institute analysis of the same pair already exists. A PDAC-specific audit needs a genuinely distinct question, a model-overlap ledger, sufficient new independent donors or an explicitly narrower technical endpoint, and transparent uncertainty. [Chan et al., 4 July 2025](https://doi.org/10.1038/s41588-025-02222-1) · [Accessible article, section “Assessment of CDS1 expression and CDS2 essentiality”](https://api.repository.cam.ac.uk/server/api/core/bitstreams/f7d2f327-8fde-44aa-b09e-67aa11ffa9e0/content)
4. An additional July 2026 preprint predicts CDS2 dependency in skin cancer using a genome-scale metabolic model. An October 2026 ovarian cancer paper reports an association with disease progression and perturbation experiments. These are model-specific and lineage-specific evidence relevant to assessing novelty. Neither validates a PDAC treatment. [Metabolic model preprint](https://doi.org/10.64898/2026.06.30.735578) · [Ovarian cancer study](https://doi.org/10.1002/cam4.72309)

## Final 27-day surveillance

Across the three filters, 29 source identifiers represent 24 distinct reports. Five PubMed preprint identifiers duplicate five Europe PMC preprint records exactly by digital object identifier. There were 23 distinct preprints and one published systematic review. Of the 24 distinct reports, 17 preprints met substantive eligibility, one preprint provides large-animal model context and six reports were excluded. The single systematic review addressed prognosis and was first published online in October, although the PubMed issue-date query returned it. Neither database returned a record under the randomised-controlled-trial publication-type filter in this particular window. Incomplete indexing and keyword scope preclude interpreting that zero as clinical inactivity. See the [record-by-record decisions](november-screen.tsv).

| Theme | Current observations and impact on the research choice |
|---|---|
| Dependencies | A preprint finds a hybrid basal/classical phenotype with a candidate dependency. Potential confounder for a dichotomous subtype analysis. Evidence is preclinical. [1 November](https://doi.org/10.21203/rs.3.rs-11519779/v1) |
| KRAS | Allelic imbalance and loss of the wild-type allele in metastatic models and human samples make mutant-versus-wild-type classification an incomplete exposure. The preprint does not show patient benefit from manipulating allelic balance. [20 November](https://doi.org/10.64898/2026.11.18.767567) |
| Resistance | An arrest-associated expression score recurred in two untreated PDAC atlases and did not track cell-line drug sensitivity or bulk survival. A successful association across transcriptomic cohorts need not translate to treatment response. [6 November](https://doi.org/10.64898/2026.11.04.764269) |
| Microenvironment | A preprint reports a fibroblast population supporting antitumour activity in a particular immune setting. Another reports stromal conditioning in biopsy-derived organoids. Record tumour/stroma composition and whether a sample preserves its microenvironment before transferring a cell-intrinsic result. [4 November](https://doi.org/10.64898/2026.11.03.764075) · [26 November](https://doi.org/10.64898/2026.11.25.769316) |
| Repurposing and combinations | Four PDAC organoids and four cell lines supported preclinical testing of TR-107 and capivasertib. A separately indexed PubMed copy is the same preprint. Single-agent screens cannot independently validate a combination effect. [17 November](https://doi.org/10.64898/2026.11.13.766013) |
| RNA therapeutics | Preprints already address microRNA-based reversal of resistance and RNA-targeting interventions. Neither establishes that abstract secondary-structure design predicts drug activity. [10 November](https://doi.org/10.64898/2026.11.07.765071) · [19 November](https://doi.org/10.64898/2026.11.18.767627) |
| Computational target discovery | A preprint integrates inherited variation, transcriptomics, single-cell data and dependency screens for midkine. Disease-risk associations and reanalyses of shared public cohorts require different validation from treatment-response predictions. [16 November](https://doi.org/10.64898/2026.11.12.766325) |

## Historically indexed reviews and phase III evidence

The seven-theme vocabulary yielded 100 distinct records indexed as systematic reviews (99 in PubMed, 91 in Europe PMC, 90 common) and 16 indexed phase III reports (16 in PubMed, 15 in Europe PMC, 15 common). There was no overlap between these two sets. All 116 have a recorded screening decision. Forty-nine syntheses, five primary trial reports, seven secondary trial analyses and nine context reports were retained. Forty-two records were excluded. Four mixed-cancer papers await access to full-text results sufficient to assess PDAC eligibility. Several reviews overlap in primary trials, and indexing a review as systematic does not establish low risk of bias. See the [queries](historical/queries.tsv), [identifier membership](historical/membership.tsv.gz) and [screening decisions](historical-screen.tsv).

* **Mechanistic evidence and trial results can diverge.** Six randomised trials of vascular endothelial growth factor or receptor inhibition in a published pancreatic cancer meta-analysis yielded no overall survival advantage. A separate pancreatic cancer cisplatin combination trial enrolled 400 patients and reported an overall survival hazard ratio of 1.10 (95% confidence interval 0.89–1.35). Both provide cautionary clinical comparators for promising laboratory combinations. [Stromal/vascular review](https://doi.org/10.1007/s11523-018-0578-x) · [GIP-1 trial](https://doi.org/10.1200/JCO.2009.25.4433)
* **A marker measured after assigning treatment can be prognostic without predicting benefit from that treatment.** In the PA.3 molecular subset, the treatment-by-KRAS interaction had a reported P value of 0.38. In MPACT, tumour stromal protein measurement was available in only 256 of 861 enrolled patients and failed to identify benefit from nab-paclitaxel. These are examples of both restricted denominators and weak transportability. [PA.3 biomarker study](https://doi.org/10.1002/cncr.25393) · [MPACT biomarker study](https://pubmed.ncbi.nlm.nih.gov/26169969/)
* **Observed treatment response depends on the comparator.** A 2026 review covered eight first-line checkpoint-combination studies with 379 patients. A single-arm pooled objective response of 38% coexisted with an absence of definitive survival benefit in randomised comparisons. A separate review of 46 preclinical cytokine studies identified xenograft and subcutaneous model limits and unclear-to-high risk of bias. These populations and endpoints answer different questions. [Clinical synthesis](https://doi.org/10.3389/fimmu.2026.1855859) · [Preclinical synthesis](https://doi.org/10.1016/j.ijbiomac.2026.153486)
* **There is substantial prior art in both subtype and RNA target prioritisation.** A systematic review already studied tumour subtyping across 15 studies and 2,731 patients. A 2026 review prioritised 16 candidate messenger RNA vaccine antigens from public data and experimental work. Neither identifies performance of inverse folding as a validated surrogate for treatment response. [Subtyping review](https://doi.org/10.1016/j.hpb.2024.02.001) · [RNA prioritisation review](https://doi.org/10.3389/fimmu.2026.1803792)

The themed phase III filter captured only 16 of the 225 records found by removing the seven topic-term requirements while retaining pancreatic disease terms and the phase III publication type. This is a measured sensitivity limitation. Of the 225 disease-only records, 88 were classified as treatment reports, 94 as associated trial reports, eight require adjudication and 35 were excluded. See the separate [phase III review and trial-family links](phase3/README.md) and [queries](phase3/queries.tsv). The restricted November filter also missed the phase III daNIS-2 trial, published on 9 November, which did not show a benefit from adding NIS793 to chemotherapy. The database count of zero in the restricted slice cannot stand in for an absence of new clinical evidence. [daNIS-2](https://pubmed.ncbi.nlm.nih.gov/43002828/)

## Reproduction

Python 3.12.14 and standard-library modules only. The retrievals traversed all returned identifier pages, checked the number of unique identifiers against each API-reported hit count and retained sorted-set SHA-256 (Secure Hash Algorithm 256-bit) digests. Study selection is a recorded human-readable judgement. Running the retrieval script again will regenerate record memberships, not adjudicate clinical eligibility. The following commands run from the repository root. Use new output directories for live searches.

```sh
python3 literature/search/verify.py
python3 -O literature/search/verify.py
python3 literature/search/phase3/verify_trials.py
python3 literature/search/retrieve.py --output /tmp/pcr001-index-rerun
python3 literature/search/retrieve.py --output /tmp/pcr001-november-rerun --only preprints_update reviews_update trials_update
python3 literature/search/retrieve.py --output /tmp/pcr001-historical-rerun --only phase3 systematic_reviews
```

For a literature update, preserve this snapshot, specify a new cut-off and search dates, repeat native queries, inspect revised versions and retractions, and report additions and withdrawals by identifier. The biomedical application programming interfaces can update their underlying records. See [PubMed utilities](https://www.ncbi.nlm.nih.gov/books/NBK25501/) and [Europe PMC public service](https://europepmc.org/RestfulWebService).
