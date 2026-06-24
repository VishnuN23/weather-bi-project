import sqlite3
import pandas as pd

# Connect to database
conn = sqlite3.connect("weather.db")

# SQL query
query = """
SELECT
    COUNT(*) AS total_records,
    AVG(temperature) AS avg_temperature,
    MAX(temperature) AS max_temperature,
    MIN(temperature) AS min_temperature,
    AVG(humidity) AS avg_humidity
FROM weather_data;
"""

df = pd.read_sql(query, conn)

print(df)

conn.close()