# Weather BI Project

## Project Overview
This project collects weather data from an API, stores it in PostgreSQL, and visualizes it using Power BI.

## Technologies Used
- Python
- PostgreSQL 16
- Power BI Desktop
- Pandas
- Psycopg2
- OpenWeatherMap API

## Project Workflow

1. Extract weather data from API
2. Save data into CSV
3. Load CSV into PostgreSQL
4. Connect Power BI to PostgreSQL
5. Create dashboard visualizations

## Database Schema

Table: weather_data

| Column | Type |
|----------|----------|
| id | SERIAL |
| city | VARCHAR(50) |
| country | VARCHAR(10) |
| temperature | FLOAT |
| humidity | FLOAT |
| pressure | FLOAT |
| wind_speed | FLOAT |
| weather_main | VARCHAR(50) |
| weather_description | VARCHAR(100) |
| collection_time | TIMESTAMP |

## Dashboard Visualizations

- Temperature by City (Bar Chart)
- Weather Conditions (Donut Chart)
- Temperature vs Humidity (Scatter Plot)
- Average Temperature (Gauge)
- Treemap by City
- World Map Visualization
- Data Table

## Project Structure

weather-bi-project/
│
├── data/
├── scripts/
├── screenshots/
├── dashboard/
├── README.md
└── weather.db
## Setup

1. Clone the repository

git clone https://github.com/VishnuN23/weather-bi-project.git

2. Install dependencies

pip install -r requirements.txt

3. Create a .env file

OPENWEATHER_API_KEY=your_api_key_here

4. Run data extraction

python scripts/extract_weather.py

5. Load data into PostgreSQL

python scripts/load_to_postgres.py

6. Open Power BI Dashboard

dashboard/Weather_BI_Dashboard.pbix
## Author

Vishnu Nanda Kumar