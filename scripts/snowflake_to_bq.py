import duckdb
import pandas as pd

# Connect to DuckDB (simulated Snowflake)
con = duckdb.connect(database='data/snowflake.db', read_only=True)

# Read transformed table
df = con.execute("SELECT * FROM analytics_table").df()

# Save as CSV (simulating BigQuery)
df.to_csv("data/bigquery_table.csv", index=False)

print("Data exported to data/bigquery_table.csv (simulated BigQuery)")
