# Cursor Cloud Agent Prompt: Card-Krueger Issue Task

Use this template when assigning an issue-scoped task to Cursor Cloud Agent.
Replace bracketed fields before sending.

```text
Repository: meleantonio/AC4E_Padova
Issue: #[number] - [title]
Base branch: main
Work branch: [agent/short-issue-name]

Read AGENTS.md, GUIDE.md, examples/card-krueger/README.md,
examples/card-krueger/docs/data_source_map.md, and the issue body first.

Allowed files:
- [repo-relative path]

Out of scope:
- Do not edit examples/card-krueger/data/synthetic_fast_food_panel.csv.
- Do not inspect .env, secrets/, data/raw/, or data/private/.
- Do not make substantive causal claims from the synthetic teaching data.

Acceptance criteria:
- [ ] [mechanically checkable criterion]
- [ ] [verification command or static check]
- [ ] Synthetic-data caveat remains visible.

Workflow:
1. Create or switch to the work branch named above.
2. Make the smallest coherent change.
3. Use /research-sdd for planning if empirical code, data documentation, or
   paper claims change.
4. Use a read-only reviewer subagent before opening the PR:
   replication-verifier, identification-reviewer, data-reviewer, or pr-reviewer.
5. Open a PR to main.

PR body must include:
- changed files;
- issue number;
- verification command output or UNABLE TO CHECK with reason;
- reviewer subagent used and verdict;
- remaining risks or human checks.
```

## Reviewer Agent Choice

- Use `replication-verifier` for runnable examples, dependencies, and tests.
- Use `identification-reviewer` for empirical strategy, assumptions, or causal
  wording.
- Use `data-reviewer` for data maps, variable coding, and sample restrictions.
- Use `pr-reviewer` for final scope/privacy review.

## Model Choice

Use the default inherited model for scoped edits. Use a higher-reasoning model
only for identification review, multi-file orchestration, or ambiguous empirical
claims. Use a faster model for read-only inventory checks that do not change
research interpretation.
