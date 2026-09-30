# Weather Data API

A Python-based weather application that retrieves real-time weather data using the Open-Meteo API.

## Description

This project retrieves weather information for cities using Open-Meteo's geocoding and weather APIs.

It supports both single-city weather reports and comparisons between multiple cities. The project also includes a reusable API client for handling HTTP requests and a FastAPI interface for exposing the weather functionality through HTTP endpoints.

## Features

- Search for a city by name
- Geocode city names using Open-Meteo
- Retrieve current temperature
- Retrieve relative humidity
- Retrieve wind speed
- Get weather information for a single city
- Compare weather data across multiple cities
- Calculate average temperature
- Identify the hottest city
- Identify the highest recorded temperature in the comparison
- Handle invalid or unavailable cities
- Reusable API client for HTTP communication
- FastAPI endpoints for accessing weather data
- JSON-based weather result handling

## Technologies Used

- Python
- Requests
- Open-Meteo API
- FastAPI
- Uvicorn
- python-dotenv
- Git & GitHub

## Project Structure

```text
weather/
├── api_client.py
├── weather.py
├── main.py
├── cli.py
├── fastapi_test.py
├── requirements.txt
└── README.md
