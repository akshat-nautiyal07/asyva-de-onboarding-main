# 03 Python (Batch ETL)

## Objective
Write clean Python ETL scripts with logging, validation, and re-runnable behavior.

## Assignment
### Tasks
Build a small batch ETL:
1. Extract: read CSV from `data/input/`
2. Transform:
   - handle nulls
   - cast types
   - basic validations (duplicate keys, required columns)
3. Load: write cleaned output to `data/output/` (CSV or Parquet)
4. Add logging + exception handling.
5. Keep code modular (functions, not one giant script).

### Learning links
- Python official tutorial: https://docs.python.org/3/tutorial/
- pandas intro tutorials: https://pandas.pydata.org/docs/getting_started/intro_tutorials/


## Expected outputs (acceptance criteria)
- `etl_csv/extract.py`, `transform.py`, `load.py`, `pipeline.py`
- Logs are produced (stdout or log file)
- `README.md` includes how to run + sample commands


## Mentor review checklist
- Is code modular and readable?
- Does it fail loudly with useful errors?
- Can it be rerun without manual cleanup?
