# Verification Loop

Use this loop for cloud-agent branches, local app goals, and reviewer
subagents. The goal is to avoid open-ended repair cycles.

## Loop Contract

1. Plan: restate scope, allowed files, forbidden files, acceptance criteria, and
   verification commands.
2. Implement: make only the smallest changes needed for the issue.
3. Verify: run the listed commands or provide a precise reason they could not
   run.
4. Review: ask the matching reviewer to return green, yellow, or red.
5. Decide: merge, fix once more, stop, or open a new issue.

Maximum iterations: three. After three failed or incomplete cycles, stop and
open a follow-up issue with evidence.

## Verdicts

| Verdict | Meaning | Action |
| --- | --- | --- |
| GREEN | Acceptance criteria pass, evidence is present, reviewer found no blockers. | PR is ready for human review and possible merge. |
| YELLOW | Main artifact is usable but evidence is incomplete, a command was unavailable, or a caveat remains. | Human decides whether to merge with risk noted or open a follow-up issue. |
| RED | Scope breach, failed verification, unsafe data access, missing core criterion, or economics overclaim. | Do not merge. Fix within scope once, or open a new issue. |

## Evidence Table

Copy this into the PR body.

| Iteration | Agent action | Verification | Reviewer verdict | Decision |
| --- | --- | --- | --- | --- |
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |

## Exit Rules

GREEN exit:

- all acceptance criteria are checked;
- command output or artifact paths are included;
- reviewer verdict is green;
- remaining risks are minor and named.

YELLOW exit:

- task is useful but one non-critical check is unavailable;
- missing evidence is stated plainly;
- a follow-up issue is opened or explicitly deferred.

RED exit:

- the agent touched forbidden files;
- the task needs private data, secrets, or a login not provided;
- tests or scripts fail for task-related reasons;
- claims go beyond the synthetic teaching data;
- official docs contradict the instructions;
- the loop has reached three iterations without green.

## New Issue Triggers

Open a new issue instead of expanding the current one when:

- acceptance criteria need another file or folder;
- a reviewer asks for a different task type;
- a dependency or account setup is needed;
- the code path needs refactoring beyond the current branch;
- the economics question changes.

## Minimal PR Decision Comment

```text
Decision: GREEN / YELLOW / RED
Issue:
Branch:
Verification:
Reviewer:
Remaining risk:
Follow-up issue:
```
