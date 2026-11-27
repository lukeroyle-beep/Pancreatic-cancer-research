# Search and screening | PCR-005

**Run date** 27 November 2026. **Question** Which publications have already proved, tested or materially constrained a transfer from base-pair maximisation to stack or Turner models? The principal unit was a study or publicly deposited research artifact. Related reports are linked and classified by status. Two abstract-index queries and forward citation tracking supplement the seed and publisher full-text searches. Formal and empirical claims were extracted separately.

## Indexed searches executed

The [screening ledger](rna-screening.tsv) contains the original record identifiers, publication dates, classifications, source links, retrieval route and reason for every inclusion or exclusion from the indexed searches. The union including the seed and one supplemental preprint comprises 25 records (9 direct inclusions, 4 adjacent methods, 2 contextual predecessors, 10 exclusions). This count does not include every web result or foundational comparator used as a citation. No quantitative synthesis or independent duplicate screening was performed.

| Route (public application programming interface) | Returned records | Notes |
|---|---:|---|
| Europe PubMed Central (Europe PMC), broad query below | 11 | One page, 100 requested. |
| Europe PMC, model-sensitive query below | 12 | One page, 1,000 requested. Non-RNA materials/protein false positives are retained in the ledger. |
| Europe PMC, author probe below | 0 | Failed to retrieve known work. Retained as a weak query, without inferring absence. |
| PubMed via Entrez, query below | 6 | The interface explicitly dropped unmatched quoted phrases “RNA designability” and “undesignable RNA”. PubMed identifier 41648297 is a bioRxiv preprint and duplicates the Europe PMC preprint record. |
| Europe PMC citations to MED/41137157 | 2 | One review and one article predating the journal version. [Citation endpoint](https://www.ebi.ac.uk/europepmc/webservices/rest/MED/41137157/citations?format=json) |
| OpenAlex citations to W4399114806 | 5 | Includes the 2026 proceedings and the two-short-helices preprint. Also includes two records predating the journal issue. Use publisher dates for chronology; the conference paper appeared on 27 August 2026. [Citing records](https://api.openalex.org/works?filter=cites:W4399114806&per_page=50&select=id,doi,display_name,type,publication_date) |
| OpenAlex citations to the 2026 proceedings, W7162983694 | 0 | Zero at retrieval, limited by indexing latency. [Citing records](https://api.openalex.org/works?filter=cites:W7162983694&per_page=50&select=id,doi,display_name,type,publication_date) |

For Europe PMC, pass the query alone as the `query` parameter to [the REST search endpoint](https://www.ebi.ac.uk/europepmc/webservices/rest/search), with `format=json`, `resultType=lite` and `pageSize=1000` (100 for the broad query). PubMed used `db=pubmed`, `retmode=json`, `retmax=500` and the query as `term` on [Entrez search](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi). Identifiers and totals may change as indexing is revised. Dates in the ledger are record-specific and need not be print issue dates.

**Europe PMC, broad**

```text
(TITLE_ABS:"RNA inverse folding" OR TITLE_ABS:"inverse RNA folding" OR TITLE_ABS:"RNA designability" OR TITLE_ABS:"undesignable RNA" OR (TITLE:RNA AND TITLE:"inverse folding")) AND FIRST_PDATE:[2025-10-25 TO 2026-11-27]
```

**Europe PMC, model-sensitive**

```text
(TITLE_ABS:"inverse folding" OR TITLE_ABS:designability) AND (TITLE_ABS:stacking OR TITLE_ABS:stacked OR TITLE_ABS:separability OR TITLE_ABS:"ensemble") AND FIRST_PDATE:[2025-10-25 TO 2026-11-27]
```

**Europe PMC, author probe**

```text
(AUTH_FIRST:"Boury T" OR AUTH_FIRST:"Jogalekar A") AND (TITLE_ABS:"RNA" OR TITLE_ABS:folding) AND FIRST_PDATE:[2025-10-25 TO 2026-11-27]
```

**PubMed**

```text
("RNA inverse folding"[Title/Abstract] OR "inverse RNA folding"[Title/Abstract] OR "RNA designability"[Title/Abstract] OR "undesignable RNA"[Title/Abstract] OR (RNA[Title] AND "inverse folding"[Title])) AND ("2025/10/25"[Date - Publication] : "2026/11/27"[Date - Publication])
```

## Supplementary discovery and novelty challenge

For forward discovery the indexed literature and web search of publisher pages, arXiv, bioRxiv, author records and proceedings used the following literal queries among others. The direct conference follow-up emerged through author/title search and OpenAlex. The ranked web interface does not guarantee stable ordering or complete recall.

```text
"RNA inverse folding can be solved in linear time" citation November 2026 RNA Boury modulo stochastic RNA design Turner stacking
"linearbpdesign" OR "modulo-separability" OR "modulo-2 separated" RNA after:2025-10-24 before:2026-11-28
site:arxiv.org RNA inverse folding energy model secondary structure stack maximization nearest neighbor guarantees after:2025-10-24 before:2026-11-28
"RNA inverse folding under stacked base pair maximization" after:2026-08-27 before:2026-11-28 weighted Turner design "locked" further publications
RNA inverse folding weighted sequence-dependent stacking energy design certificate three-helix Watson–Crick family "stacking" mathematical 2026 before:2026-11-28
RNA "inverse folding" stacking "weighted" November 2026 after:2026-09-30 before:2026-11-28 author Boury Ponty Huang weighted stack certificate three helix
Boury RNA inverse folding publications fall 2026 November stacked base pair maximization separability mathematics after:2026-08-27 before:2026-11-28
"three-helix" "stacking-only" RNA inverse folding certificate weighted family "Royle"
"Fast and Versatile RNA Design" Tianshuo Zhou latest after:2026-03-01 before:2026-11-28 journal publication DOI RivalDesigner
```

Include work with an identifiable model and a designability theorem, experimental comparison, model-specific impossibility result, or relevant secondary-structure benchmark. Include peer-reviewed studies and separately identifiable preprints. Retain foundational older papers through citation following. Exclude protein inverse folding, unrelated materials, primary three-dimensional backbone representation claims and articles with a different biological endpoint. For clinical context use PDAC primary studies, assessed in PCR-001. Screened journal abstracts and preprints do not certify formal proofs or computational reproducibility.

**Closest competing work.** The 2026 stack maximisation paper directly addresses the direction highlighted in 2025; it also benchmarks Turner, so an unqualified “first” on either point is untenable. Jogalekar reports a restricted base-pair extension. Zhou and colleagues derive motif and ensemble results. The same group’s FastDesign preprint proposes a two-stage computational method and evaluates both MFE and ensemble endpoints. Other methods include constraint programming, initialisation strategies, probabilistic pseudoknot design and learning-based approaches. The March preprint must be treated as a preprint unless a peer-reviewed version is verified. [WABI 2026](https://doi.org/10.4230/LIPIcs.WABI.2026.12) · [Jogalekar](https://arxiv.org/abs/2608.25194) · [Ensemble bounds](https://doi.org/10.1093/bioinformatics/btag246) · [FastDesign preprint](https://arxiv.org/abs/2603.02283) · [Earlier exact seeding study](https://doi.org/10.1007/978-3-031-90252-9_9) · [2026 review](https://doi.org/10.1093/bib/bbag327)

We found no later source in these searches establishing the owner's exact weighted numerical certificate under the same model and family, or proving a general Turner extension. This is a scoped search result. It remains to reconcile the owner's definitions with the WABI weighted-case discussion, examine alternative terminology and mathematicians' thesis/preprint repositories, and obtain independent technical review. The two-index citation lists demonstrate why one unqualified count would be misleading. Title/abstract restrictions, nonindexed software, incomplete citation coverage and preprint versions limit any priority claim.
