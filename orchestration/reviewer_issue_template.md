# Reviewer Issue Template

Use this as a PR comment, issue comment, or read-only subagent prompt. Reviewers
should find blockers before style suggestions.

````markdown
## Review Target

- PR or branch:
- Related issue:
- Files to review:
- Reviewer role:

## Read-Only Rule

Do not edit files. Do not run commands that write outputs unless explicitly
listed below. Do not access private data, secrets, `.env`, or confidential
manuscripts.

## What To Check

- Scope: every change is inside the issue's Allowed Files.
- Data safety: no private data, secrets, raw external data, or invented sources.
- Economics: treatment, comparison group, timing, outcome, units, and sample restrictions are accurate.
- Claims: no causal or policy claim goes beyond the synthetic teaching design.
- Verification: commands or artifacts in the PR body match the files changed.
- Docs: official-doc claims are linked in `docs/sources.md` when version-sensitive.

## Acceptance Criteria Under Review

- [ ] [Paste the issue acceptance criterion.]
- [ ] [Paste the issue acceptance criterion.]
- [ ] [Paste the issue acceptance criterion.]

## Optional Commands

Only run these commands if the environment is already prepared:

```bash
[read-only or expected-output command]
```

## Verdict Format

Return one verdict:

- GREEN: acceptance criteria pass, evidence is present, no blockers.
- YELLOW: usable with named caveats or missing non-critical evidence.
- RED: blocker, unsafe scope, failed verification, or overclaim.

Then report:

- Blockers first, with file references.
- Evidence checked.
- Commands run or not run.
- Questions for the human.
- Suggested follow-up issue if the fix is outside this PR.
````

## Reviewer Role Map

| Tool lane | Reviewer role | Use when |
| --- | --- | --- |
| Codex | `replication-verifier` | Check commands, tests, outputs, and reproducibility claims. |
| Codex | `identification-data-reviewer` | Check data maps, treatment, comparison group, outcome, and caveats. |
| Codex | `pr-scope-reviewer` | Check branch scope, PR evidence, and merge readiness. |
| Claude Code | `replication-verifier` | Same as Codex replication review. |
| Claude Code | `identification-reviewer` | Check identification and overclaiming. |
| Claude Code | `data-reviewer` | Check source, unit, variables, and restrictions. |
| Claude Code | `pr-reviewer` | Check PR contract and evidence. |
| Cursor | `replication-verifier` | Same as Codex replication review. |
| Cursor | `identification-reviewer` | Check identification and overclaiming. |
| Cursor | `data-reviewer` | Check source, unit, variables, and restrictions. |
| Cursor | `pr-reviewer` | Check PR contract and evidence. |
