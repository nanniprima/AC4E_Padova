# Claude Code Harness For Economics Research

This folder is the portable source pack for the Padova Claude Code CLI and
desktop app lanes. Copy the pieces into a disposable research project after
reading them.

Official Claude Code docs checked on 2026-06-24:

- Overview: <https://code.claude.com/docs/en/overview>
- Skills: <https://code.claude.com/docs/en/skills>
- Subagents: <https://code.claude.com/docs/en/sub-agents>
- Hooks: <https://code.claude.com/docs/en/hooks>
- Settings: <https://code.claude.com/docs/en/settings>
- MCP: <https://code.claude.com/docs/en/mcp>
- Sessions: <https://code.claude.com/docs/en/manage-sessions>

## Install Map

| Asset | Portable source | Project-native path |
| --- | --- | --- |
| Project instructions | `CLAUDE.md` | `CLAUDE.md` |
| Skills | `skills/<name>/SKILL.md` | `.claude/skills/<name>/SKILL.md` |
| Subagents | `agents/<name>.md` | `.claude/agents/<name>.md` |
| Settings and hooks | `hooks/settings.example.json` | `.claude/settings.json` |
| Hook scripts | `hooks/*.py` | `.claude/hooks/*.py` |
| MCP example | `mcp/mcp.json.example` | `.mcp.json` at repo root; uses `agent-harness/mcp/fred/` |
| Checkpoint prompts | `goals/*.md`, `orchestration/*.md` | paste into a Claude session |

For a disposable project:

```bash
cp -R examples/card-krueger /tmp/ck-claude-demo
cd /tmp/ck-claude-demo
mkdir -p .claude/skills .claude/agents .claude/hooks
cp -R /path/to/AC4E_Padova/agent-harness/claude/skills/* .claude/skills/
cp /path/to/AC4E_Padova/agent-harness/claude/agents/*.md .claude/agents/
cp /path/to/AC4E_Padova/agent-harness/claude/hooks/*.py .claude/hooks/
cp /path/to/AC4E_Padova/agent-harness/claude/hooks/settings.example.json .claude/settings.json
cp /path/to/AC4E_Padova/agent-harness/claude/mcp/mcp.json.example .mcp.json
cp /path/to/AC4E_Padova/agent-harness/claude/CLAUDE.md CLAUDE.md
```

Review hooks before trusting them:

```text
/hooks
```

Review the shared FRED MCP server before enabling it:

```bash
python3 agent-harness/mcp/fred/scripts/smoke.py --offline
```

## CLI And App Notes

The CLI and desktop app share project files, settings, skills, agents, and MCP
configuration. Session history and checkpointing are surface-specific: use
`claude --continue` for CLI sessions, and app sessions/checkpoints for desktop
work unless you deliberately hand off through an official command.

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

## Safety Rules

- Settings examples deny `.env`, `secrets/`, `data/raw/`, and `data/private/`.
- Hooks are examples and are not active until copied and reviewed with `/hooks`.
- Keep API keys in environment variables; do not commit `.mcp.json` with secrets.
- The Card-Krueger CSV is synthetic teaching data. Do not claim it replicates the
  published estimates or supports a substantive causal claim.
