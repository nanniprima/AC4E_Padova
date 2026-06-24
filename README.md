# Agentic Coding for Economists - Padova, 25 June 2026

Participant-facing repository for a **5-hour hands-on workshop** at the
University of Padova. The workshop compresses the Pavia material into one
sequence that economists can use immediately on a research project.

The running example is Card and Krueger's minimum-wage study. Participants use it
to practice the same agentic workflow they can later transfer to a dissertation,
paper, replication, or teaching project.

## Start Here

1. Open [`START_HERE.md`](START_HERE.md) for the participant path.
2. Complete [`SETUP.md`](SETUP.md) before the workshop if possible.
3. Keep [`SCHEDULE.md`](SCHEDULE.md) open during the session.
4. Use [`GUIDE.md`](GUIDE.md) as the main reference.
5. Follow the tool-lane instructions in [`materials/tool_tracks.md`](materials/tool_tracks.md).
6. Run [`examples/card-krueger/`](examples/card-krueger/) for the shared
   economics example.
7. Work from [`examples/starter_article/`](examples/starter_article/) when
   building your own harness.
8. Use [`orchestration/`](orchestration/) for issue, cloud-agent, swarm, loop,
   goal, and reviewer templates.

## Course Snapshot

| Item | Padova version |
| --- | --- |
| Format | 5 hours, in person |
| Audience | Economists and economics researchers |
| Core example | `examples/card-krueger/` Card-Krueger teaching project |
| Main tools | Codex, Claude Code, Cursor, GitHub, Playwright |
| Output | Personalized research-article harness plus verification checklist |

## What Participants Produce

By the end of the session, each participant should have at least a draft of:

- a project brief and research design memo;
- an agent instruction file and privacy boundary;
- a tool-lane harness with skills, subagents, hooks, and optional MCP;
- an orchestration log for issue/branch/cloud-agent work;
- one verification or replication check;
- a short 7-day adoption plan for their own research.

## Repository Map

```text
.
+-- README.md
+-- START_HERE.md
+-- SETUP.md
+-- SCHEDULE.md
+-- SYLLABUS.md
+-- GUIDE.md
+-- docs/
|   +-- import_manifest.md
|   +-- research_article_harness.md
|   +-- sources.md
+-- materials/
|   +-- module_01_foundations.md
|   +-- module_02_hooks_goals.md
|   +-- module_03_referee_review.md
|   +-- module_04_playwright.md
|   +-- module_05_capstone.md
|   +-- tool_tracks.md
+-- tool-lanes/
|   +-- README.md
|   +-- codex-cli.md
|   +-- codex-app.md
|   +-- claude-cli.md
|   +-- claude-app.md
|   +-- cursor.md
+-- examples/
|   +-- card-krueger/
|   +-- starter_article/
|   +-- codex/
|   +-- codex-app/
|   +-- claude/
|   +-- claude-app/
|   +-- cursor/
|   +-- hooks/
|   +-- paper/
|   +-- playwright/
|   +-- web-form/
+-- orchestration/
|   +-- README.md
|   +-- cloud_agent_issue_template.md
|   +-- card_krueger_swarm.md
|   +-- verification_loop.md
|   +-- goals/
+-- notes/
|   +-- orchestration_log_template.md
+-- templates/
+-- slides/
+-- scripts/
```

## Tool Lanes

All lanes use the same research-harness ideas. Pick the surface you will
actually use:

| Lane | Surface | Starting point |
| --- | --- | --- |
| A1 | Codex CLI | `examples/codex/` |
| A2 | Codex app | `examples/codex-app/` plus `examples/codex/` |
| B1 | Claude Code CLI | `examples/claude/` |
| B2 | Claude Code app | `examples/claude-app/` plus `examples/claude/` |
| C | Cursor | `examples/cursor/` |

Detailed lane manuals live in [`tool-lanes/`](tool-lanes/).

Tool UI and configuration details change quickly. When a setup step depends on
the installed version, use the official links in [`docs/sources.md`](docs/sources.md)
and verify the label or command in your version.

## Provenance

The initial base was imported from `meleantonio/AC4E_LSE_PhD_Students`; see
[`docs/import_manifest.md`](docs/import_manifest.md). The Padova structure and
Card-Krueger guide draw on `AC4E_Pavia`; see [`docs/sources.md`](docs/sources.md).

No `followup/`, `follow_up/`, or `website/` folder is part of this participant
repository.
