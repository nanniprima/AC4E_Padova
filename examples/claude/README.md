# Claude Code Track (Lanes B1 And B2)

This folder is the project-native Claude Code example for the Padova workshop.
It is copied from
[`../../agent-harness/claude/`](../../agent-harness/claude/README.md) so
participants can install the same harness in a disposable research project.

Official docs checked on 2026-06-24:

- Claude Code skills: <https://code.claude.com/docs/en/skills>
- Claude Code subagents: <https://code.claude.com/docs/en/sub-agents>
- Claude Code hooks: <https://code.claude.com/docs/en/hooks>
- Claude Code settings: <https://code.claude.com/docs/en/settings>
- Claude Code MCP: <https://code.claude.com/docs/en/mcp>
- Claude Code sessions: <https://code.claude.com/docs/en/manage-sessions>

## Merge steps

```bash
cp -r examples/starter_article /path/to/my-article
mkdir -p /path/to/my-article/.claude/{skills,agents,hooks}
cp -r examples/claude/.claude/skills/* /path/to/my-article/.claude/skills/
cp examples/claude/.claude/agents/*.md /path/to/my-article/.claude/agents/
cp examples/claude/.claude/hooks/*.py /path/to/my-article/.claude/hooks/
cp examples/claude/.claude/settings.example.json /path/to/my-article/.claude/settings.json
cp examples/claude/.mcp.json.example /path/to/my-article/.mcp.json
cp examples/claude/CLAUDE.md /path/to/my-article/CLAUDE.md
```

Review `settings.json`, `.mcp.json`, and hook scripts before use. Run `/hooks`
to inspect and trust hooks.

## Harness Contents

| Path | Role |
| --- | --- |
| `.claude/skills/` | `research-sdd`, `replication-checker`, `referee-checklist`, `data-reviewer`, `paper-polisher`, `loop-on-verification` |
| `.claude/agents/` | `identification-reviewer`, `data-reviewer`, `replication-verifier`, `literature-reviewer`, `loop-verifier`, `pr-reviewer`, `sdd-orchestrator` |
| `.claude/settings.example.json` | permissions and hook examples |
| `.claude/hooks/` | prompt safety, pre-tool policy, verification reminder |
| `.mcp.json.example` | FRED/public-data MCP config for `agent-harness/mcp/fred/` with env vars |
| `goals/` | checkpointed Card-Krueger task prompts |
| `orchestration/` | cloud-swarm and review-loop prompts |

Optional MCP smoke test from the Padova repository root:

```bash
python3 agent-harness/mcp/fred/scripts/smoke.py --offline
```

## Sample Skill Prompt

```text
/data-reviewer

Review examples/card-krueger read-only. Check source, unit, treatment group,
comparison group, outcome, wave coding, panel balance, missing values, and
synthetic-data caveat. Do not edit files.
```

## Sample Subagent Prompt

```text
Use the replication-verifier subagent on examples/card-krueger. Review the
README, data source map, did_analysis.py, and tests. Do not edit files. Return
GREEN, YELLOW, or RED with exact evidence and command recommendations.
```

## Long-running work

Use `/goal` where available, checkpoint prompts in `goals/`, or
`claude --continue` for the same CLI session. Desktop app sessions should use app
checkpoints unless you deliberately hand off through an official command.

Claude Code app (B2) uses the same files; see
[`../claude-app/README.md`](../claude-app/README.md).
