import pandas as pd
import sqlite3

# Read CSV
df = pd.read_csv("data/raw/weather_data.csv")

# Create database
conn = sqlite3.connect("weather.db")

# Load data into SQLite
df.to_sql(
    "weather_data",
    conn,
   if_exists="append",
    index=False
)

print("Data loaded successfully!")

conn.close()