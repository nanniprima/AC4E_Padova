# Replication Package

## Requirements

- Python 3.10+
- Packages in `requirements.txt`

## Clean run (from repo root)

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/estimate_did.py
python -m pytest tests/ -q
```

Expected outputs:

- `tables/main_did.tex`
- Console print of Treat × Post coefficient

## Replication check

Use your lane's `replication-checker` skill as a read-only checklist. It should
cite the clean-run commands above, path hygiene, data documentation, generated
outputs, and remaining gaps. Do not mark the project GREEN without command
evidence.
