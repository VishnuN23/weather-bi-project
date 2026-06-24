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

## Author

Vishnu Nanda Kumar