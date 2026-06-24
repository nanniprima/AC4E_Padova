# Goal: Card-Krueger Data Map Audit

Use this goal for a cloud agent, app goal, or checkpointed CLI session.

```text
Goal: Audit and tighten the Card-Krueger data-source documentation for the
synthetic teaching example.

Context:
- Project: Padova participant repo, Card-Krueger running example.
- Data constraints: use only public source links and bundled synthetic teaching
  data. Do not access private data, raw downloaded archives, or secrets.
- Claim constraint: the synthetic example cannot support a substantive causal
  claim.

Allowed files:
- Read: GUIDE.md, docs/sources.md, examples/card-krueger/README.md,
  examples/card-krueger/docs/data_source_map.md,
  examples/card-krueger/docs/research_design_memo.md.
- Edit: examples/card-krueger/README.md,
  examples/card-krueger/docs/data_source_map.md.

Forbidden files and actions:
- Do not edit examples/card-krueger/data/synthetic_fast_food_panel.csv.
- Do not edit analysis code or tests.
- Do not read or edit .env, data/private/, data/raw/, or confidential files.
- Do not invent source URLs, sample details, or results.

Done when:
- examples/card-krueger/docs/data_source_map.md states source, access note,
  unit of observation, treatment group, comparison group, outcome, timing,
  sample restriction, transformations, raw/private data status, and research
  caveat.
- examples/card-krueger/README.md links to the data map and keeps the synthetic
  teaching-data caveat visible.
- No text claims the bundled CSV is Card and Krueger's raw data.
- No text claims the synthetic result establishes a causal or policy effect.

Verification:
- Run: python3 -m pytest examples/card-krueger/tests
- Run: rg -n "synthetic teaching data|not Card and Krueger's raw data|sample restriction|unit of observation" examples/card-krueger
- Ask a read-only identification-data reviewer to return green/yellow/red.

Stop conditions:
- Stop if verification requires private data or a live login.
- Stop if fixing the issue requires analysis code or data edits.
- Stop if official source links conflict with the existing source map.

Final response:
- Changed files.
- Checklist against the Done when criteria.
- Verification output.
- Reviewer verdict.
- Remaining risks or follow-up issue.
```
