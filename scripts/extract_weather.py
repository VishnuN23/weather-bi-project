import requests
import pandas as pd
from dotenv import load_dotenv
import os
from datetime import datetime

# Load API key
load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")
CITIES = ["Munich", "London", "Paris", "Tokyo", "New York"]

weather_records = []

for CITY in CITIES:

    url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

    response = requests.get(url)

    data = response.json()

    weather_record = {
        "city": data["name"],
        "country": data["sys"]["country"],
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "pressure": data["main"]["pressure"],
        "wind_speed": data["wind"]["speed"],
        "weather_main": data["weather"][0]["main"],
        "weather_description": data["weather"][0]["description"],
        "collection_time": datetime.now()
    }

    weather_records.append(weather_record)

df = pd.DataFrame(weather_records)

print(df)

df.to_csv("data/raw/weather_data.csv", index=False)

print("Data saved successfully!")