# Cursor Harness For Economics Research

This folder is the portable source pack for the Padova Cursor lane. Copy these
files into a disposable research project after reading them and checking your
installed Cursor version.

Official Cursor docs checked on 2026-06-24:

- Overview: <https://cursor.com/docs>
- Rules and `AGENTS.md`: <https://cursor.com/docs/rules>
- Skills: <https://cursor.com/docs/skills>
- Subagents: <https://cursor.com/docs/subagents>
- Hooks: <https://cursor.com/docs/hooks>
- MCP: <https://cursor.com/docs/mcp>
- Cloud Agent: <https://cursor.com/docs/cloud-agent>

## Install Map

| Asset | Portable source | Project-native path |
| --- | --- | --- |
| Project instructions | `AGENTS.md` | `AGENTS.md` |
| Project rules | `rules/*.mdc` | `.cursor/rules/*.mdc` |
| Skills | `skills/<name>/SKILL.md` | `.cursor/skills/<name>/SKILL.md` |
| Subagents | `agents/<name>.md` | `.cursor/agents/<name>.md` |
| Hook examples | `hooks/hooks.json` and `hooks/*.py` | `.cursor/hooks.json` and `.cursor/hooks/*.py` |
| MCP example | `mcp/mcp.json.example` | `.cursor/mcp.json`; uses `agent-harness/mcp/fred/` |
| Cloud prompts | `cloud-agent-prompts/*.md` | paste into Cursor Cloud Agent |
| Checkpoint prompts | `goals/*.md`, `orchestration/*.md` | paste into Cursor Agent or Cloud Agent |

For a disposable project:

```bash
cp -R examples/card-krueger /tmp/ck-cursor-demo
cd /tmp/ck-cursor-demo
mkdir -p .cursor/rules .cursor/skills .cursor/agents .cursor/hooks
cp -R /path/to/AC4E_Padova/agent-harness/cursor/skills/* .cursor/skills/
cp /path/to/AC4E_Padova/agent-harness/cursor/agents/*.md .cursor/agents/
cp /path/to/AC4E_Padova/agent-harness/cursor/rules/*.mdc .cursor/rules/
cp /path/to/AC4E_Padova/agent-harness/cursor/hooks/*.py .cursor/hooks/
cp /path/to/AC4E_Padova/agent-harness/cursor/hooks/hooks.json .cursor/hooks.json
cp /path/to/AC4E_Padova/agent-harness/cursor/mcp/mcp.json.example .cursor/mcp.json
cp /path/to/AC4E_Padova/agent-harness/cursor/AGENTS.md AGENTS.md
```

Review hooks and MCP server code before enabling them. Keep real API keys in
environment variables, not in tracked JSON.

Smoke-test the shared FRED MCP server before enabling it:

```bash
python3 agent-harness/mcp/fred/scripts/smoke.py --offline
```

## Included Skills

- `research-sdd`: plan a research task before editing code or prose.
- `data-reviewer`: read-only audit of data source, unit, coding, and caveats.
- `replication-checker`: clean-room reproducibility checklist.
- `referee-checklist`: pre-submission economics paper review.
- `paper-polisher`: prose edit that preserves claims and citations.
- `loop-on-verification`: bounded implement/evaluate/revise loop.

## Included Subagents

- `identification-reviewer`: DiD identification and overclaiming review.
- `data-reviewer`: data coding, panel balance, and source documentation review.
- `replication-verifier`: reproducibility and test-evidence review.
- `literature-reviewer`: bibliography and Card-Krueger source-claim review.
- `loop-verifier`: one bounded verification-loop iteration.
- `pr-reviewer`: PR scope, privacy, and interpretation review.
- `sdd-orchestrator`: spec-driven planning coordinator.

## Sample Skill Prompt

```text
/data-reviewer

Review examples/card-krueger read-only. Check source, unit, treatment group,
comparison group, outcome, wave coding, panel balance, missing values, and
synthetic-data caveat. Do not edit files.
```

## Sample Subagent Prompt

```text
Use the replication-verifier subagent on examples/card-krueger. Review the README,
data source map, did_analysis.py, and tests. Do not edit files. Return GREEN,
YELLOW, or RED with exact evidence and command recommendations.
```

## Cursor-Specific Notes

- Project rules must be `.mdc` files under `.cursor/rules/`; plain `.md` files in
  that folder are ignored by the rule system.
- Cursor also reads `AGENTS.md`; keep high-level economics boundaries there and
  use `.cursor/rules/*.mdc` for scoped workflow rules.
- Cursor discovers project skills in `.cursor/skills/` and subagents in
  `.cursor/agents/`.
- Cursor Cloud subagents use MCP servers configured for the team at
  `cursor.com/agents`; local `.cursor/mcp.json` is for the local workspace.
- Hook support and event names are version-sensitive. Treat `hooks/hooks.json` as
  a reviewed hook plan and test it in your installed Cursor version before
  relying on it for enforcement.

## Safety Rules

- Do not inspect `.env`, `secrets/`, `data/raw/`, or `data/private/` without
  explicit human approval.
- Do not commit `.cursor/mcp.json` if it contains real secrets.
- The Card-Krueger CSV is synthetic teaching data. Do not claim it replicates the
  published estimates or supports a substantive causal claim.
