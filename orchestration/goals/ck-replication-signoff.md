# Goal: Card-Krueger Replication Signoff

Use this as the final read-only or mostly read-only check after the data map,
baseline estimate, and write-up streams are merged.

```text
Goal: Produce a final replication signoff for the Card-Krueger synthetic
teaching example from current main.

Context:
- Project: Padova participant repo.
- Review target: examples/card-krueger plus relevant guide links.
- Data constraints: public links and bundled synthetic teaching data only.
- Claim constraint: no substantive causal claim from the synthetic example.

Allowed files:
- Read: GUIDE.md, docs/sources.md, examples/card-krueger/,
  docs/research_article_harness.md.
- Create or edit only: notes/card_krueger_replication_signoff.md.

Forbidden files and actions:
- Do not edit examples/card-krueger/ code, data, tests, or docs in this signoff
  branch. Open a fix issue instead.
- Do not read or edit .env, data/private/, data/raw/, or confidential files.
- Do not download external raw data.
- Do not approve merge if a blocker remains.

Done when:
- notes/card_krueger_replication_signoff.md records source status, data caveat,
  commands run, outputs checked, reviewer verdict, and follow-up issues.
- The clean run from examples/card-krueger/README.md is checked or explicitly
  marked unavailable with the reason.
- The signoff states whether the example is green, yellow, or red.
- Every blocker has a file reference and recommended follow-up issue.

Verification:
- Run: python3 examples/card-krueger/src/did_analysis.py
- Run: python3 -m pytest examples/card-krueger/tests
- Run: rg -n "synthetic teaching data|not Card and Krueger's raw data|Toy DID estimate" examples/card-krueger GUIDE.md
- Ask a read-only pr-scope reviewer or pr-reviewer to return green/yellow/red.

Stop conditions:
- Stop if commands fail for task-related reasons; write a red signoff instead
  of editing source files.
- Stop if guide links are stale and require broader workshop edits.
- Stop if any output relies on private data or live secrets.

Final response:
- Signoff file path.
- Verification output summary.
- Reviewer verdict.
- Follow-up issues.
```
