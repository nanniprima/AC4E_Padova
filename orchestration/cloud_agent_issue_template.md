# Cloud Agent Issue Template

Copy this into a GitHub issue, then assign it to a cloud/background agent. Keep
the task small enough for one branch and one PR.

````markdown
## Objective

[One concrete outcome. Example: audit the Card-Krueger data-source map and make
the synthetic-data caveat mechanically visible.]

## Agent Surface And Model

- Surface: [Codex cloud / Cursor Cloud Agent / Claude Code background session / other]
- Model choice:
  - Fast or low reasoning for mechanical link, typo, or formatting updates.
  - Medium/default reasoning for bounded docs, examples, and tests.
  - High/extended reasoning for data transformations, estimates, orchestration plans, and review tasks.
- Reason for choice: [why this task needs that level]

## Base And Branch

- Base branch: `main`
- Base commit: `[paste current main commit]`
- Work branch: `[agent/NN-short-name]`
- Related issue: `#[number]`

## Allowed Files

- [specific file or folder]
- [specific file or folder]

## Forbidden Files And Actions

- Do not read or edit `.env`, secret files, `data/private/`, or confidential manuscripts.
- Do not edit `data/raw/` or downloaded external raw data.
- Do not replace `examples/card-krueger/data/synthetic_fast_food_panel.csv` unless this issue explicitly asks for fixture changes.
- Do not invent citations, data sources, results, or command output.
- Do not broaden the branch beyond this issue.

## Acceptance Criteria

- [ ] [Mechanically checkable criterion tied to a path.]
- [ ] [Mechanically checkable criterion tied to a path.]
- [ ] Synthetic-data and no-causal-claim caveats remain visible where relevant.
- [ ] New or changed examples can be verified without live secrets or private data.

## Verification

Run, or explain exactly why you could not run:

```bash
[command 1]
[command 2]
```

Expected evidence:

- [output file, test result, grep result, screenshot, or review note]

## Reviewer

Before requesting merge, ask a read-only reviewer to use:

- Reviewer role: [replication-verifier / identification-data-reviewer / pr-scope-reviewer / data-reviewer / identification-reviewer / pr-reviewer]
- Reviewer prompt: see `orchestration/reviewer_issue_template.md`.

## Stop Conditions

Stop and report without editing further if:

- required files are missing or renamed;
- a command needs private data, secrets, or a local app login;
- acceptance requires changing files outside `Allowed Files`;
- tests fail for reasons unrelated to this task;
- official docs contradict the requested implementation.

## PR Evidence Required

The PR body must include:

- issue link and branch name;
- changed files;
- acceptance checklist with file references;
- verification commands and results;
- reviewer verdict;
- remaining risks and follow-up issues.
````

## Ready-To-Paste Codex Cloud Trigger

```text
@codex Start this issue on branch [agent/NN-short-name] from current main.
Use [fast/medium/high] reasoning because [reason]. Stay within Allowed Files and
Forbidden Files above. Open a PR when acceptance criteria pass. Include command
outputs, changed files, reviewer result, and remaining risks in the PR body. If
you hit a stop condition, comment on this issue instead of broadening scope.
```

## Generic Cloud/Background Trigger

```text
Start the task described in this issue on branch [agent/NN-short-name]. Treat the
issue body as the contract. Do not access private data or secrets. Do not edit
outside Allowed Files. Run the listed verification or explain why it cannot run.
Open a PR only when the acceptance criteria pass and include the required
evidence.
```
