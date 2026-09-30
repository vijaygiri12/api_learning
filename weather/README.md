# Weather Data API

A Python-based weather application that retrieves real-time weather
data using the Open-Meteo API.

## Features

- Search weather data by city name
- Geocoding using Open-Meteo
- Retrieve temperature, humidity, and wind speed
- Compare weather data across multiple cities
- Calculate average temperature
- Identify the hottest city
- Save weather results as JSON
- FastAPI endpoint for accessing weather data
- Uses a reusable API client for HTTP requests

## Project Structure

```text
weather/
├── api_client.py
├── weather.py
├── main.py
├── cli.py
├── fastapi_test.py
├── data.json
├── weather.txt
└── README.md
