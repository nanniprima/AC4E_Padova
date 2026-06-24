# Goal: Card-Krueger Baseline Estimate Review

Use this goal for the stream that checks the runnable teaching analysis and its
evidence.

```text
Goal: Verify that the Card-Krueger synthetic baseline analysis runs, writes the
documented summary, and keeps its research caveat visible.

Context:
- Project: Padova participant repo, Card-Krueger running example.
- Data constraints: use only examples/card-krueger/data/synthetic_fast_food_panel.csv.
- Claim constraint: the output is a toy difference-in-differences estimate for
  teaching, not a replication of the published paper.

Allowed files:
- Read: examples/card-krueger/README.md, examples/card-krueger/src/did_analysis.py,
  examples/card-krueger/tests/test_did_analysis.py,
  examples/card-krueger/docs/data_source_map.md,
  examples/card-krueger/docs/research_design_memo.md.
- Edit only if needed: examples/card-krueger/src/did_analysis.py,
  examples/card-krueger/tests/test_did_analysis.py,
  examples/card-krueger/README.md.
- Generated output: examples/card-krueger/outputs/baseline_did_summary.md.

Forbidden files and actions:
- Do not change the synthetic CSV unless a separate fixture issue authorizes it.
- Do not add external data downloads.
- Do not store API keys or credentials.
- Do not claim the toy estimate reproduces the AER paper.

Done when:
- python3 examples/card-krueger/src/did_analysis.py prints
  "Toy DID estimate: 3.0 FTE workers."
- examples/card-krueger/outputs/baseline_did_summary.md exists after the run.
- python3 -m pytest examples/card-krueger/tests passes.
- The output note includes the source status, unit, outcome, sample restriction,
  transformations, and research caveat.
- Any code or test edit is directly tied to the criteria above.

Verification:
- Run: python3 examples/card-krueger/src/did_analysis.py
- Run: python3 -m pytest examples/card-krueger/tests
- Run: rg -n "Toy DID estimate: 3.0 FTE workers|synthetic teaching data|does not certify a causal claim" examples/card-krueger
- Ask a read-only replication verifier to return green/yellow/red.

Stop conditions:
- Stop if pandas or pytest is unavailable and report the missing dependency.
- Stop if a fix requires changing the data fixture.
- Stop if the expected estimate changes for reasons not explained by an
  authorized fixture issue.

Final response:
- Changed files.
- Command output summary.
- Path to the generated summary.
- Reviewer verdict.
- Remaining risks or follow-up issue.
```
