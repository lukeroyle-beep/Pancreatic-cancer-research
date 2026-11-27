# PCR-005 | Existing research and reusable assets

**Audit date:** 27 November 2026. **Source:** the owner's public [Bioinformatics repository at 512777e4b72a412e80af1dc1f6ea40bb820e3522][upstream], dated 11 October 2026. The cancer repository's [founding note][foundation] left this location unresolved. It is a separately maintained project. References here point back to its source.

## What the existing proof establishes

One target class has a formal result. An outer helix encloses two hairpins, with no unpaired junction positions. Each of three helix lengths and two loop lengths independently ranges over every integer at least three. For the construction specified in the source, the target uniquely minimises the model energy and the best distinct admissible fold lies exactly **0.93 kilocalories per mole higher**. The bound holds over every admissible competitor, including isolated pairs, arbitrary admitted topologies and the empty fold. Removing the outermost pair attains the bound. The final theorem supplies both the universal lower bound and an attaining witness. Its inputs impose no upper bound on structure size. The proof's model uses pseudoknot-free partial matchings, Watson–Crick pairing, at least three enclosed positions in each pair, and only adjacent nested stacks. It uses 16 oriented entries from a fixed two-decimal table based on Turner 2004 at 37 °C. [Formal final statements][final] · [Model definitions][model] · [Parameter provenance][parameters] · [Historical internal verification report][verified]

This is a restricted, constructive answer to a stacking-energy design question. The proof gives neither a general test for modulo-separability under stacking energies nor a linear-time complexity theorem for Turner energies. The source gives its construction cost informally. Allowing wobble or adding hairpin, internal loop, multiloop, terminal or coaxial terms can change the ordering. A gap between the two lowest distinct energies alone cannot specify target ensemble probability: this also depends on the number and energies of all conformations. Biological stability, cell delivery and a therapeutic effect in pancreatic ductal adenocarcinoma (PDAC) are separate questions. [Original conditions and proof boundary][verified] · [Boury et al., 2025][boury25] · [Boury et al., 2026][boury26]

## Asset register

| Asset and status | What can be reused now | Limitation and next verification |
|---|---|---|
| [Frozen specification][spec] and [parameters][parameters] | Cite the pairing, span, energy units and orientation as a named mathematical comparator. The parameter file provides a source, date, temperature and exact integer model identifier. | Resolve rights for any table redistribution. Verify orientation against the primary parameter table before testing another engine. Experimental uncertainty is outside the model. |
| [Three-helix proof package][lean] and [final declarations][final] | Cite the pinned theorem and audit it in the original repository. Ten Lean modules connect actual stack energies, counting bounds and reconstruction of the full competing fold. | The conditional intermediate arithmetic result alone does not imply the theorem. Inspect the final declarations and their hypotheses. The older partial Stage 4 report predates their completion. |
| [Proof checker][verifier] and [11 October receipt][receipt] | Historical build, version, source hashes and theorem-by-theorem axiom output support exact replication. Three final properties cover uniqueness, lower bound and attainment. | Require the verified flag, both named final theorems, expected declaration count and admissible axiom set, alongside a successful exit code. The wrapper's success status on its own does not enforce the final theorem flag. |
| [Seven-position pilot and independent assessment][pilot] | A separate, single-instance Lean sanity check with six possible folds and 20 declarations provides a small comparison case. | It proves that instance only. It does not verify the Python recurrence or the full family. |
| [Model parser, dynamic programming and exhaustive enumeration][src] | Conceptual baseline plus a separate topology/energy oracle for short instances. The interval algorithm retains the two lowest distinct levels, ties and example structures. The oracle has an independent table transcription. | These routines do not calculate a partition function. The scoring/oracle agreement alone cannot establish the fidelity of shared conventions. Do not port source until rights and provenance are resolved. |
| [Bounded validation and junction runners][tests], [finite receipt][finite] and [junction results][junction] | Existing reference results, deterministic controls and known failure cases. The finite validation covers 87,893 sequence cases and 306,648 compatible folds, exhausting all sequences through length eight and sampling 128 per length at lengths nine through twelve. | The number of rows is not the number of independent biological observations. Standard historical Python validation uses assertions, which can be disabled by optimised execution. These runners write to tracked result locations, so use only a disposable original checkout for a future rerun. |
| [Stage 3 grid][grid], [stress batch][stress], [independent enumeration][enum] and [earlier construction failure][negative] | Immutable historical cases with ground truth under the frozen model. The failed construction supplies a tie control. The 243-point grid and 26 stress cases supply regression cases for the later construction. | These are correlated variants of one topology. They cannot estimate population-level performance or provide a held-out biological cohort. |
| [Internal proof review][internal] and [dated prior-art comparison][comparison] | Reviewers can trace the proof history and compare the 2026 International Conference on Algorithms for Bioinformatics paper's assumptions on wobble, span, helix length, weights and isolated competitors. | Internal agent review provides no independent external endorsement. The 2026 authors also discuss weighted stacking. Model differences alone cannot establish priority or that their result implies ours. |

## Checks performed in this audit

* Enumerated all 10 repositories returned under the owner's connected GitHub account; the next inventory page was empty. Checked the recursive default-branch trees of the cancer, Bioinformatics and Mathematics repositories. The Bioinformatics tree was complete, its branch listing contained only `main`, and its pull request listing returned zero items. An owner-scoped exact-phrase code search returned no hits despite the source being present; repository inventory and direct tree inspection located it. This coverage cannot rule out unindexed code elsewhere or offline records. Private records were used for chronology only. Public claims here can be checked without access to them.
* Recomputed Secure Hash Algorithm 256-bit (SHA-256) digests for all **10 source files and 14 command/axiom logs** enumerated in the 11 October receipt. All **24/24** match. The receipt records 14 successful command exits, 100 theorem declarations, and final dependencies limited to `Classical.choice`, `Quot.sound` and `propext`. Inspected the actual final declarations, admissibility predicate, two independent scorer implementations and checker logic. The published commit pins Lean 4.19.0. [Receipt][receipt] · [Final axiom output][axioms] · [Verification entry point][verifier]
* Recounted outcomes from archived individual rows, without generating sequences or running a folding experiment. For the fixed 256-candidate junction screen there are **225 unique minima, two ties and 29 beaten targets**. For the old four-case loop extension there are **two ties and two unique minima**. All 243 grid rows and all 26 stress rows have a unique minimum and an alternative-minus-target energy of 93 model units. The seven exhaustive cross-check rows sum to **466,653** admissible folds: 397,815 across six retained cases plus 68,838 in the failed control. The failed control has three optima. These are checks on reported outcomes in one repository, not new biological or independent computational validation. [Junction rows][junction] · [Old construction][old] · [Grid][grid] · [Stress][stress] · [Independent enumeration][enum]

To repeat the receipt-integrity check in a disposable original checkout at the exact revision above, run the following from its root. Use a Python interpreter in normal mode.

```sh
python3 - <<'PY'
from pathlib import Path
from hashlib import sha256
import json

base = Path("results/stage4/github_publication_20261011/verification")
receipt = json.loads((base / "verification.json").read_text())
entries = [(Path(name), value) for name, value in receipt["sources"].items()]
entries.extend((base / item["log"], item["sha256"]) for item in receipt["commands"])
for path, expected in entries:
    if sha256(path.read_bytes()).hexdigest() != expected:
        raise SystemExit(f"Checksum mismatch for {path}")
if len(entries) != 24:
    raise SystemExit("Unexpected number of receipt entries")
print(f"Matched {len(entries)} archive entries")
PY
```

## Fresh proof reproduction

A new Linux x86-64 checkout of the original public source was pinned to `512777e4b72a412e80af1dc1f6ea40bb820e3522`. The test used the official [Lean 4.19.0 release](https://github.com/leanprover/lean4/releases/tag/v4.19.0), its bundled Lake build tool and Python 3.12.14. The tests used deterministic formalisation and no experimental dataset or random seed. The verifier compiled the pilot and family packages in their original repository. The generated [proof reproduction receipt](proof-reproduction.json) records the compiler build, archive size and measured checksum, source hashes, individual command exit codes, log hashes and final axiom checks.

Clean builds reproduced **20 Stage 2 declarations** and **100 Stage 4 declarations**. The per-theorem axiom dependencies and all audited source hashes match their archived records. The final declarations explicitly establish `unique_minimum`, `gap_lower_bound` and `exact_gap`. The Stage 4 verifier checked for prohibited proof shortcuts and required a recorded axiom report for every theorem. The tracked checkout was clean after the build. This is an independent rerun of the upstream proof using its existing formalisation and verifier. A separate formalisation and external review remain outstanding.

Reproduce the compilation in a disposable checkout, from its root, after selecting the exact upstream commit and putting the pinned `lean` and `lake` executables on the path. Each output directory must be new. The public release record did not supply a publisher checksum for the Linux archive; the SHA-256 recorded here identifies the bytes used.

```sh
git rev-parse HEAD
lean --version
lake --version
python3 scripts/verify_lean.py --output-dir /tmp/pcr-proof-stage2-run
python3 scripts/verify_stage4.py --output-dir /tmp/pcr-proof-stage4-run
```

## Reuse decision and relevance

Use the existing theorem as a mathematical positive control and the retained tie as a negative control for future methodology. Both are already documented. The complete source tree contains no visible licence file. No permission to redistribute code, proof scripts, tables or benchmark records into the cancer repository was established during this audit. Links, attribution and independently written descriptions suffice for this stage. Ownership of the source account does not resolve every component's rights. [Pinned tree][upstream] · [GitHub licensing guidance][licensing]

The plausible PDAC connection is downstream quality control of folding assumptions, conditional on a credible RNA (ribonucleic acid) modality and independently measured structural or functional outcomes. No eligible PDAC-specific readout, molecule, delivery experiment or clinical validation accompanies this theorem. Assign high confidence to the theorem's stated model scope and the checked archive identity, and low confidence to therapeutic transfer. Novelty beyond this family and published 2026 results is unresolved. Any proposal for a new mathematical project or for experiments in a therapeutic setting requires a separate scientific case. [Verified owner report][verified] · [2026 prior art][boury26]

[upstream]: https://github.com/lukeroyle-beep/Bioinformatics/tree/512777e4b72a412e80af1dc1f6ea40bb820e3522
[foundation]: https://github.com/lukeroyle-beep/Pancreatic-cancer-research/blob/ce4111ef71096bcf63fa22e423789d4060192dde/research/PCR-005/README.md
[final]: https://github.com/lukeroyle-beep/Bioinformatics/blob/512777e4b72a412e80af1dc1f6ea40bb820e3522/lean/Stage4/Final.lean
[model]: https://github.com/lukeroyle-beep/Bioinformatics/blob/512777e4b72a412e80af1dc1f6ea40bb820e3522/lean/Stage4/Model.lean
[parameters]: https://github.com/lukeroyle-beep/Bioinformatics/blob/512777e4b72a412e80af1dc1f6ea40bb820e3522/parameters.json
[verified]: https://github.com/lukeroyle-beep/Bioinformatics/blob/512777e4b72a412e80af1dc1f6ea40bb820e3522/research/STAGE4_VERIFIED_REPORT.md
[spec]: https://github.com/lukeroyle-beep/Bioinformatics/blob/512777e4b72a412e80af1dc1f6ea40bb820e3522/sources/STAGE1_SPEC.md
[lean]: https://github.com/lukeroyle-beep/Bioinformatics/tree/512777e4b72a412e80af1dc1f6ea40bb820e3522/lean/Stage4
[verifier]: https://github.com/lukeroyle-beep/Bioinformatics/blob/512777e4b72a412e80af1dc1f6ea40bb820e3522/scripts/verify_stage4.py
[receipt]: https://github.com/lukeroyle-beep/Bioinformatics/blob/512777e4b72a412e80af1dc1f6ea40bb820e3522/results/stage4/github_publication_20261011/verification/verification.json
[axioms]: https://github.com/lukeroyle-beep/Bioinformatics/blob/512777e4b72a412e80af1dc1f6ea40bb820e3522/results/stage4/github_publication_20261011/verification/Final_axioms.log
[pilot]: https://github.com/lukeroyle-beep/Bioinformatics/blob/512777e4b72a412e80af1dc1f6ea40bb820e3522/results/stage2_verification/independent_review_final.md
[src]: https://github.com/lukeroyle-beep/Bioinformatics/tree/512777e4b72a412e80af1dc1f6ea40bb820e3522/src
[tests]: https://github.com/lukeroyle-beep/Bioinformatics/tree/512777e4b72a412e80af1dc1f6ea40bb820e3522/tests
[finite]: https://github.com/lukeroyle-beep/Bioinformatics/blob/512777e4b72a412e80af1dc1f6ea40bb820e3522/results/validation.json
[junction]: https://github.com/lukeroyle-beep/Bioinformatics/blob/512777e4b72a412e80af1dc1f6ea40bb820e3522/results/junction_pilot.json
[grid]: https://github.com/lukeroyle-beep/Bioinformatics/blob/512777e4b72a412e80af1dc1f6ea40bb820e3522/results/stage3/separated_gc_grid.json
[stress]: https://github.com/lukeroyle-beep/Bioinformatics/blob/512777e4b72a412e80af1dc1f6ea40bb820e3522/results/stage3/separated_gc_stress.json
[enum]: https://github.com/lukeroyle-beep/Bioinformatics/blob/512777e4b72a412e80af1dc1f6ea40bb820e3522/results/stage3/exhaustive_checks.json
[negative]: https://github.com/lukeroyle-beep/Bioinformatics/blob/512777e4b72a412e80af1dc1f6ea40bb820e3522/results/stage3/counterexample.json
[old]: https://github.com/lukeroyle-beep/Bioinformatics/blob/512777e4b72a412e80af1dc1f6ea40bb820e3522/results/stage3/original_loop_check.json
[internal]: https://github.com/lukeroyle-beep/Bioinformatics/blob/512777e4b72a412e80af1dc1f6ea40bb820e3522/results/stage4/continuation_20261009/final_independent_review.md
[comparison]: https://github.com/lukeroyle-beep/Bioinformatics/blob/512777e4b72a412e80af1dc1f6ea40bb820e3522/research/STAGE4_LITERATURE.md
[boury25]: https://doi.org/10.1186/s13015-025-00278-6
[boury26]: https://doi.org/10.4230/LIPIcs.WABI.2026.12
[licensing]: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository
