# Example Provenance

Sanitized copies for teaching. No API keys or personal paths.

| Workshop path | Source | Notes |
| --- | --- | --- |
| `examples/card-krueger/` | Adapted from Pavia `examples/card-krueger-toy/` plus verified public Card-Krueger source links | Synthetic teaching data; cleaned for Padova path and tests |
| `starter_article/.cursor/` | Padova `agent-harness/cursor/` adapted from Pavia and official Cursor docs | Complete Cursor-native rules, skills, subagents, hooks, and MCP example |
| `examples/hooks/.codex/` | Course-authored | SessionStart / PreToolUse / PostToolUse |
| `agent-harness/codex/` | Adapted from Pavia harness and checked against official Codex docs on 2026-06-24 | Portable Codex skills, subagents, hooks, MCP config, goals, orchestration |
| `agent-harness/claude/` | Adapted from Pavia harness and checked against official Claude Code docs on 2026-06-24 | Portable Claude skills, subagents, settings/hooks, MCP config, goals, orchestration |
| `agent-harness/cursor/` | Adapted from Pavia harness and checked against official Cursor docs on 2026-06-24 | Portable Cursor rules, skills, subagents, hooks, MCP config, goals, orchestration, Cloud Agent prompts |
| `agent-harness/mcp/fred/` | Course-authored, checked against MCP and FRED docs on 2026-06-24 | Stdlib-only public-data MCP example with offline smoke test |
| `examples/cursor/.cursor/mcp.json.example` | Template only | Uses `${env:FRED_API_KEY}` for the bundled FRED server; do not commit secrets |
| `examples/plugins/README.md` | Cursor marketplace docs | Optional superpowers / doc-sync plugins |

Lane folders (`codex/`, `claude/`, `cursor/`) mirror harness **skills and agents** in native paths; merge into a copy of `starter_article/`.
