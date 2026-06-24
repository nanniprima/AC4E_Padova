# Cursor Track (Lane C)

Merge these files into your copy of [`starter_article/`](../starter_article/) or
inspect [`../../agent-harness/cursor/`](../../agent-harness/cursor/) as the
portable source pack.

## Merge steps

```bash
cp -r examples/starter_article /path/to/my-article
cp -r examples/cursor/.cursor /path/to/my-article/
cp examples/cursor/AGENTS.md /path/to/my-article/AGENTS.md   # if starting fresh
```

Optional: `cp examples/cursor/.cursor/mcp.json.example /path/to/my-article/.cursor/mcp.json`.
Keep `FRED_API_KEY` in your environment; do not commit real API keys.

## Harness files

| Path | Role |
| --- | --- |
| `AGENTS.md` | Project-level research boundaries |
| `.cursor/rules/economics-research.mdc` | Scoped economics research rule |
| `.cursor/rules/cloud-agent-prs.mdc` | Cloud Agent PR discipline |
| `.cursor/skills/data-reviewer/` | Data source, coding, and panel audit |
| `.cursor/skills/loop-on-verification/` | Bounded implement-review-revise loop |
| `.cursor/skills/paper-polisher/` | Claim-preserving prose polish |
| `.cursor/skills/referee-checklist/` | Pre-submission review |
| `.cursor/skills/replication-checker/` | Clean-run gate |
| `.cursor/skills/research-sdd/` | Plan before empirics/LaTeX edits |
| `.cursor/agents/data-reviewer.md` | Read-only data reviewer |
| `.cursor/agents/identification-reviewer.md` | DiD/IV/RD critique |
| `.cursor/agents/literature-reviewer.md` | Card-Krueger citation/source check |
| `.cursor/agents/loop-verifier.md` | One verification-loop iteration |
| `.cursor/agents/pr-reviewer.md` | Scope/privacy PR review |
| `.cursor/agents/replication-verifier.md` | Reproducibility and tests review |
| `.cursor/agents/sdd-orchestrator.md` | Spec-driven planning coordinator |
| `.cursor/hooks.json`, `.cursor/hooks/` | Version-sensitive hook examples |
| `.cursor/mcp.json.example` | FRED/public-data MCP config for `agent-harness/mcp/fred/` |
| `.cursor/environment.json` | Optional Cloud Agent bootstrap |
| `goals/` | Ready-to-paste Card-Krueger goal prompts |
| `orchestration/` | Review-loop and swarm prompts |
| `cloud-agent-prompts/` | Issue-scoped Cursor Cloud Agent prompt |

Cursor docs checked on 2026-06-24 place project rules in `.cursor/rules/*.mdc`,
skills in `.cursor/skills/`, subagents in `.cursor/agents/`, and project MCP
configuration in `.cursor/mcp.json`. Hook examples are version-sensitive; read
the installed Cursor hook docs before relying on `.cursor/hooks.json` for
enforcement.

Optional MCP smoke test from the Padova repository root:

```bash
python3 agent-harness/mcp/fred/scripts/smoke.py --offline
```

## Exercise

```text
Read examples/starter_article/AGENTS.md and merge examples/cursor/.cursor into my
starter_article copy. List the Cursor skills, reviewer subagents, hook examples,
and MCP template I should invoke in Module 2.
```

Playwright: always from a terminal (`examples/playwright/`).
