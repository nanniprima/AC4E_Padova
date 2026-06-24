# Data Source Map

| Source | URL / path | Access | Variables | Notes |
| --- | --- | --- | --- | --- |
| Workshop panel (demo) | `data/raw/city_month_panel.csv` | In repo | `log_emp`, `treat`, `post` | Synthetic — Module 3 empirics |
| Public form demo (Playwright) | `http://localhost:8000` | Local server | Form fields | Module 4: run `examples/playwright/fill_demo_form.py` |
| FRED (optional MCP) | <https://fred.stlouisfed.org/> via `agent-harness/mcp/fred/` | API key in env for live calls; offline sample otherwise | e.g. `UNRATE` metadata | Copy your lane MCP example; document any series used |

## Playwright evidence (Module 4)

After running the form demo, add a row:

| Field | Value |
| --- | --- |
| Screenshot / log path | `outputs/playwright_form_evidence.txt` |
| Date captured | [YYYY-MM-DD] |
