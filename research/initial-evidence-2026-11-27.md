# Initial evidence dossier — 2026-11-27
Status: preliminary scoping, NOT a completed systematic review. No gate passed, no experiments or independent review. Baseline ce4111ef71096bcf63fa22e423789d4060192dde; README, AGENTS, ethics, licensing and programme read. Existing four-gate programme differs from owner six-gate instructions; use stricter combined requirements pending reconciliation.

## 1 Literature and search record
Web searches on 27 November 2026: "pancreatic cancer KRAS dependency CRISPR drug resistance PDAC 2026 daraxonrasib literature"; "pancreatic cancer RNA vaccine Rojas 2025 Nature pancreatic cancer organoid drug screening"; "RNA inverse folding Boury modulo separability stacking Turner 2026"; "DepMap 2026 release PRISM GDSC TCGA CPTAC pancreatic dataset"; "RNA inverse folding 2026 modulo separability Turner stacking energy RNA design Boury"; "ViennaRNA license RNA inverse folding software Eterna benchmark Rfam"; "pancreatic cancer microenvironment single cell atlas organoid drug response Tiriac CPTAC 140 PDAC". Selected relevant primary studies and methods reviews; exclude unrelated cancers without applicability, opinion-only and unverifiable claims. Search hit counts, full screening and preprint coverage not established. Next: PubMed, Europe PMC, ClinicalTrials.gov, bioRxiv, arXiv; export complete records, deduplicate, dual screen, record exclusions and dates.
* https://doi.org/10.1038/s41591-026-04537-w (Nature Medicine, 11 Aug 2026): paired circulating tumour DNA in 44 patients; 26 acquired pathway alterations, 16 KRAS amplification. Absence of detected alterations does not prove nongenetic resistance.
* https://doi.org/10.1158/0008-5472.CAN-25-1835 (Cancer Research 2026): inhibitor-anchored genetic screens across four KRAS alleles. Generic resistance screens are not novel.
* https://doi.org/10.1158/0008-5472.CAN-26-1181 (Cancer Research Nov 2026): allele-specific daraxonrasib resistance already investigated.
* https://doi.org/10.1016/j.cell.2021.11.017 (Cell Dec 2021): microenvironment-dependent plasticity and response in matched organoids and biopsies; culture bias is material.
* https://doi.org/10.1038/s41586-024-08508-4 (Nature Feb 2025): early trial vaccine immune responders 8 versus 8 nonresponders; association, not proof of efficacy.
Drug repurposing, combinations, synthetic lethality, immune evasion and computational discovery require dedicated systematic searches.

## 2 Gap register and 4 qualitative opportunity ranking
Provisional ordinal ranks, not measured scores. Criteria: clinical relevance, novelty, feasibility, data quality, independent verification.
1. Cross-platform transportability of PDAC dependencies by allele and cell state. High relevance/feasibility; novelty uncertain, quality/verification conditional on overlap. Known screens above; unresolved generalisability. DepMap and independent perturbation screens; organoid perturbation and normal-cell selectivity needed eventually.
2. Cell-state concordance across cultures and tumours. High relevance, moderate feasibility; prior Cell work limits novelty. GEO and tumour cohorts; donor-level independent validation and subsequent perturbation needed.
3. Drug response concordance across GDSC and PRISM. Moderate relevance/feasibility; assay and compound overlap may limit quality. Single-drug response cannot establish synergy; independent dose-response and combination experiments later.
4. Mathematical separability extension. High computational feasibility, indirect clinical relevance; novelty pending literature and asset audit. Exact exhaustive small-instance verification and independent proof review; eventual biochemical validation separate.
No originality established.

## 3 Dataset inventory (candidate, not acquired)
DepMap https://depmap.org/portal/data_page/ : genetic dependency, mutation, expression; twice-yearly release. exact release and PDAC counts pending. Copy-number artefacts, lineage, batch and shared cell lines.
GDSC https://www.cancerrxgene.org/ : drug response, assay and dose differences; release/count/terms pending.
PRISM https://depmap.org/portal/ : pooled viability screens; release/count/terms pending, overlap with DepMap and pooling bias.
TCGA and CPTAC https://portal.gdc.cancer.gov/ : portal reports release 46.0 Aug 10 2026; cohort-specific counts and versions pending; restricted raw data excluded, purity and stage confounding. Tumour expression is not functional dependence. CPTAC proteomics also https://proteomic.datacommons.cancer.gov/.
GEO https://www.ncbi.nlm.nih.gov/geo/ : accession-specific rights, donor counts and methods pending; batch and donor pseudoreplication.
PDB https://www.rcsb.org/ : structure-specific coverage, construct and ligand bias; snapshot/count/terms pending.
For each acquire only permitted data; record access date, exact release, file hash, license, eligible unique models and overlap before any analysis.

## 5 RNA audit and 6 assets
Boury et al 24 Oct 2025 https://doi.org/10.1186/s13015-025-00278-6: base-pair model, modulo-m algorithm O(n m 2^m), modulo-2 guarantee for designable targets with helices >=3. Empirical Turner evaluation already performed; merely repeating that observation is not novel. https://gitlab.inria.fr/amibio/linearbpdesign author implementation, license and revision not verified, no import.
2026 review https://doi.org/10.1093/bib/bbag327 identifies RNAinverse, Infrared, DesiRNA and others. Follow up undesignable motifs literature and preprint https://arxiv.org/abs/2606.07562 (Montparnasse; review status unverified). No conclusion about supersession.
ViennaRNA https://www.tbi.univie.ac.at/RNA/ external folding/ensemble baseline. EternaBench https://pmc.ncbi.nlm.nih.gov/articles/PMC9839360/ reports 12,711 chemical mapping and 7,228 switch molecules; rights and nonpathogenic subset pending. Existing owner assets not located: GitHub repository searches for RNA and code search inverse folding returned empty. Not evidence of absence. No prior proof, code or test verified. Obtain exact repository/branch and inventory before reuse. No sequences designed.

## 7 Licensing
Existing latest commit message adds Apache-2.0, while LICENSING.md still describes proposal pending approval; verify actual scope and owner decision. CC BY 4.0 prose/figures proposal not enacted here. ViennaRNA https://www.tbi.univie.ac.at/RNA/ViennaRNA/doc/html/license.html updated 26 Oct 2026 contains fee redistribution restriction and attribution; do not relicense or bundle as Apache-only. External separately installed executable is candidate, subject to license review. Eterna https://eternagame.org/about/software distinguishes licensed resources; do not assume all freely redistributable. No third-party material copied.

## 8 Risks
High: duplicated research (systematic novelty search), small PDAC strata (power and no-go rules), overlapping cell lines (group splits), tumour/culture mismatch (independent validation), restricted data (manifest), license ambiguity (owner approval), mathematical model mismatch (explicit objective and counterexamples), clinical overclaim (specialist review). All unresolved.

## 9 90-day roadmap
Days 1–20 systematic searches and asset recovery; gate 1 only with documented unresolved question. Days 21–35 data manifests, overlap/power and licensing; gate 2. Days 36–50 published controls reproduced; gate 3. Days 51–70 only approved preregistered original analysis; gate 4. Days 71–85 independent falsification; gate 5. Days 86–90 review package if justified; gate 6. Schedule conditional; no promised discovery.

## 10 Codex assignments (paste-ready)
PCR-002 feasibility: Fetch latest main, read all instructions and this dossier if merged; branch separately. Do not run discovery. Inventory exact DepMap and independent published PDAC perturbation datasets using legal public access. Record hashes/releases/rights, unique cell lines by allele, shared models, missingness, assay and confounding, power and overlap. Define held-out independent validation and preregister endpoint, effect size, uncertainty, multiple-testing correction, positive/negative controls and stop criteria. No claims of synthetic lethality from single perturbation. Publish reproducible manifest and draft PR, no merge. Stop if no independent data or adequate power.
PCR-005 audit: Fetch latest main, read instructions; locate owner's inverse folding repositories and records, pin commits and audit proofs, tests, benchmark licenses and provenance. Search citations to Boury and recent motif/stacking/Turner papers; establish exact novelty. No code import without rights; no patient or pathogen sequences. On abstract nonpathogenic structures only, specify published base-pair objective and energy-model distinctions; propose independent exhaustive small-instance oracle and positive/negative controls; preregister comparison with compatible controls and established methods, ensemble metrics, length/family splits, runtime and seeds. Reproduce only published controls after approval of gates. Report counterexamples and gaps, never equate predictions with therapeutic effect. Open draft PR, no merge.
