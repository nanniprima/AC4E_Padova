# Card-Krueger Swarm Plan

This plan turns the running example into small branch-sized tasks. A swarm is a
dependency plan, not a single giant prompt. Each row should become one issue and
one branch.

## Model Choice Rules

| Task type | Suggested model class | Why |
| --- | --- | --- |
| Link checks, typo fixes, README wiring | Fast or low reasoning | Mechanical and easy to verify. |
| Data maps, teaching docs, templates | Medium/default reasoning | Needs context but limited inference. |
| Estimation code, tests, orchestration, replication review | High/extended reasoning | Higher risk to correctness and claims. |

## Streams

| Stream | Scheduling label | Blocked by | Branch | Suggested model | Allowed files | Reviewer | Verification |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Data map and source audit | Sequential start | None | `ck/data-map-audit` | Medium | `examples/card-krueger/README.md`, `examples/card-krueger/docs/data_source_map.md` | `identification-data-reviewer` or `data-reviewer` | `python3 -m pytest examples/card-krueger/tests` |
| Cleaning and validation checks | Sequential | Data map and source audit | `ck/cleaning-validation` | High | `examples/card-krueger/src/did_analysis.py`, `examples/card-krueger/tests/` | `replication-verifier` | `python3 -m pytest examples/card-krueger/tests` |
| Baseline estimate evidence | Sequential | Cleaning and validation checks | `ck/baseline-estimate` | High | `examples/card-krueger/src/did_analysis.py`, `examples/card-krueger/outputs/`, `examples/card-krueger/tests/` | `replication-verifier` | `python3 examples/card-krueger/src/did_analysis.py` and tests |
| Source note or literature context | Parallel | Data map source URLs only | `ck/source-note` | Medium | `examples/card-krueger/docs/research_design_memo.md`, `docs/sources.md` | `identification-reviewer` | Link check or reviewer note |
| Teaching write-up | Sequential | Baseline estimate evidence | `ck/teaching-writeup` | Medium | `examples/card-krueger/docs/research_design_memo.md`, `examples/card-krueger/README.md` | `pr-scope-reviewer` or `pr-reviewer` | `rg "synthetic teaching data|Toy DID estimate" examples/card-krueger` |
| Replication package audit | Sequential | Baseline estimate evidence and teaching write-up | `ck/replication-audit` | High | `examples/card-krueger/README.md`, `examples/card-krueger/tests/`, `docs/research_article_harness.md` | `replication-verifier` | Full listed clean run from the README |
| Final review and merge plan | Sequential | All streams | `ck/final-review` | High for review, no edits by default | PR bodies, issue comments, changed files | `pr-scope-reviewer` or `pr-reviewer` | Green/yellow/red table across all streams |

## Merge Order

1. Merge data map and source audit.
2. Merge cleaning and validation checks.
3. Merge baseline estimate evidence.
4. Merge source note or literature context if it does not conflict.
5. Merge teaching write-up.
6. Merge replication package audit.
7. Run final review from `main` and open follow-up issues for anything yellow or red.

## Issue Prompts

Use `cloud_agent_issue_template.md` for each stream. Paste only one stream into
the issue and keep its branch name unique.

Example objective:

```text
Audit the Card-Krueger data-source documentation. Make sure source, unit,
treatment group, comparison group, timing, outcome, sample restriction, and
synthetic-data caveat are explicit in examples/card-krueger/README.md and
examples/card-krueger/docs/data_source_map.md. Do not edit analysis code or data.
```

Example reviewer prompt:

```text
Use orchestration/reviewer_issue_template.md as a read-only
identification-data review. Return blockers first. Check that the data map and
README still say the bundled CSV is synthetic teaching data and cannot support a
substantive causal claim.
```

## Coordination Rules

- Parallel tasks may run at the same time only if their allowed files do not
  overlap.
- Sequential tasks start after the blocking PR is merged into `main`.
- If two agents edit the same file, merge the lower-risk documentation PR first,
  rebase the second branch, and rerun its verification.
- If an agent needs a new dependency, private data, a new external source, or a
  broader claim, stop and open a follow-up issue.
