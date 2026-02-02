import pandas as pd
import duckdb

# Read CSV from data folder (simulated S3)
df = pd.read_csv("data/sample_data.csv")

# Connect to DuckDB (simulated Snowflake)
con = duckdb.connect(database='data/snowflake.db', read_only=False)

# Create staging table
con.execute("CREATE TABLE IF NOT EXISTS raw_table AS SELECT * FROM df")

# Transform: simple aggregation
con.execute("""
CREATE OR REPLACE TABLE analytics_table AS
SELECT name, SUM(amount) AS total_amount
FROM raw_table
GROUP BY name
""")

print("Data transformed in DuckDB (simulated Snowflake)")
