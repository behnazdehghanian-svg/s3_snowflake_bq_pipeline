<<<<<<< HEAD
# Local S3 → Snowflake → BigQuery Simulation

## Project Overview
This project simulates a full data engineering pipeline locally:

1. CSV files (simulating S3)
2. Load & transform using DuckDB (simulating Snowflake)
3. Export to CSV (simulating BigQuery)

## Tech Stack
- Python
- Pandas
- DuckDB
- Faker
- SQL

## How to Run
1. Install dependencies: `pip install pandas duckdb faker`
2. Generate sample data: `python scripts/generate_data.py`
3. Load & transform: `python scripts/local_to_snowflake.py`
4. Export to BigQuery: `python scripts/snowflake_to_bq.py`
5. Check `data/bigquery_table.csv` for final output
=======
# s3_snowflake_bq_pipeline
Local simulation of S3 → Snowflake → BigQuery pipeline
>>>>>>> 5b8fe2b84a5d9aa81e2aefaa7e9a822a0a1645ee
