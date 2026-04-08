# 01 SQL

## Objective
Become production-ready in SQL for analytics + pipelines.

## Assignment
Use a sample dataset (you can use any of these):
- PostgreSQL locally (recommended) OR
- SQLite locally OR
- Snowflake trial OR
- Mode SQL tutorial datasets

### Tasks
A) Basics
- Filtering, ordering, LIMIT
- Aggregations (COUNT, SUM, AVG)
- NULL handling (COALESCE)

B) Joins
- INNER vs LEFT JOIN
- Find unmatched rows (anti-join patterns)

C) Advanced
- CTEs
- Window functions (ROW_NUMBER, LAG/LEAD)
- Dedup patterns (keep latest per key)

### Practice links
- Mode SQL Tutorial: https://mode.com/sql-tutorial/
- LeetCode Database problems: https://leetcode.com/problemset/database/


## Expected outputs (acceptance criteria)
- `basics.sql` (10–15 queries, commented)
- `joins.sql` (at least 6 queries; include “customers with no orders”)
- `window_functions.sql` (include ROW_NUMBER + LAG/LEAD example)
- `deduplication.sql` (dedup using window; keep latest record)
- `README.md` explains what each file demonstrates


## Mentor review checklist
- Can you explain why window functions are used vs GROUP BY?
- Can you explain how your dedup query chooses the winning row?
