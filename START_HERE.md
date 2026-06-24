# Start Here

Use this file during the workshop when you are unsure where to go next.

## Before The Workshop

1. Read [`SETUP.md`](SETUP.md).
2. Install or update one main agentic coding tool: Codex, Claude Code, or Cursor.
3. Confirm you can open this repository locally.
4. If setup is incomplete, still attend. You can follow the demos and work in
   Markdown templates during the session.

## During The Workshop

Keep these files open:

- [`SCHEDULE.md`](SCHEDULE.md) - live timing and outputs.
- [`GUIDE.md`](GUIDE.md) - explanations and copy-paste prompts.
- [`materials/tool_tracks.md`](materials/tool_tracks.md) - Codex, Claude Code,
  and Cursor lanes.
- [`tool-lanes/`](tool-lanes/) - detailed lane manuals for CLI/app surfaces.
- [`examples/card-krueger/`](examples/card-krueger/) - shared runnable economics
  example.
- [`examples/starter_article/`](examples/starter_article/) - shared mini repo.
- [`orchestration/`](orchestration/) - cloud-agent issues, swarms, loops, goals,
  and reviewer prompts.
- [`docs/research_article_harness.md`](docs/research_article_harness.md) - final
  checklist.

## The Main Path

1. Choose a tool lane.
2. Run `examples/card-krueger/` to see the workshop's baseline DiD example.
3. Copy or work from `examples/starter_article/`.
4. Add project instructions and privacy boundaries.
5. Build a small harness: skills, subagents, hooks, optional MCP, and a goal or
   cloud-agent task.
6. Use the Card-Krueger example to practice a research design memo and
   verification loop.
7. Transfer the checklist to one real project of your own.

## Expected Outputs

| Output | Where to look |
| --- | --- |
| Runnable Card-Krueger example | `examples/card-krueger/` |
| Project brief | `templates/project_brief.md` or `examples/starter_article/docs/project_brief.md` |
| Design memo | `templates/research_design_memo.md` or `examples/starter_article/docs/research_design_memo.md` |
| Agent instructions | `templates/AGENTS_economics.md` |
| Tool-lane manual | `tool-lanes/` |
| Tool-lane harness | `examples/{codex,claude,cursor}/` |
| Orchestration templates | `orchestration/` |
| Orchestration log | `notes/orchestration_log_template.md` or `examples/starter_article/notes/orchestration_log.md` |
| Review log | `templates/review_log.md` |
| Final checklist | `docs/research_article_harness.md` |

## If You Get Lost

- If setup is broken, read the file and write the artifact manually.
- If the agent makes broad suggestions, narrow the prompt to one file and one
  output.
- If a tool label differs from the slides, trust the official docs and your
  installed version.
- If a result affects research interpretation, stop and review it yourself.
