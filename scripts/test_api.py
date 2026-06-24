import requests
from dotenv import load_dotenv
import os

# Load values from .env
load_dotenv()

# Read API key
API_KEY = os.getenv("OPENWEATHER_API_KEY")

# City to test
CITY = "Munich"

# API URL
url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

# Send request
response = requests.get(url)

# Convert response to JSON
data = response.json()

# Print result
print(data)