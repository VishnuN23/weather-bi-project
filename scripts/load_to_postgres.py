import pandas as pd
import psycopg2

df = pd.read_csv("data/raw/weather_data.csv")

conn = psycopg2.connect(
    host="localhost",
    database="weather_db",
    user="postgres",
    password="sreevalsam123",
    port="5432"
)

cur = conn.cursor()

for _, row in df.iterrows():
    cur.execute("""
    INSERT INTO weather_data
    (
        city,
        country,
        temperature,
        humidity,
        pressure,
        wind_speed,
        weather_main,
        weather_description,
        collection_time
    )
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """,
    (
        row["city"],
        row["country"],
        row["temperature"],
        row["humidity"],
        row["pressure"],
        row["wind_speed"],
        row["weather_main"],
        row["weather_description"],
        row["collection_time"]
    ))

conn.commit()

print("✅ Data loaded into PostgreSQL!")

cur.close()
conn.close()