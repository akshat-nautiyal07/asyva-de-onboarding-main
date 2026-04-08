# 00 Foundations

## Objective
- Build core data engineering mental models (OLTP vs OLAP, ETL vs ELT, batch vs streaming)
- Understand Medallion architecture (Bronze/Silver/Gold)

## Assignment
1. Read/watch the provided resources (see links section below).
2. Create a simple architecture diagram:
   `Source → Bronze → Silver → Gold`
3. Write `architecture.md` answering (in your own words):
   - Why raw data should not be queried directly?
   - What changes between Bronze, Silver, Gold?
   - Where data quality checks should live and why?
4. Commit diagram + notes to this repo.

### Learning links
- Databricks Medallion Architecture: https://www.databricks.com/glossary/medallion-architecture
- Snowflake ETL vs ELT guide: https://www.snowflake.com/guides/etl-vs-elt/


## Expected outputs (acceptance criteria)
- `architecture.md` (1–2 pages, practical explanation, no copy/paste)
- `medallion_diagram.png` (clear labeled diagram)


## Mentor review checklist
- Can you explain each layer without reading notes?
- Can you give 2 real examples of issues caught in Silver (duplicates, nulls, bad types)?
