# Weather Data API

A Python-based weather application that retrieves current weather data using the Open-Meteo API.

The project supports single-city weather reports, multi-city comparisons, a command-line interface, and a FastAPI web API.

## Features

- Search weather by city name
- Retrieve temperature, humidity, and wind speed
- Compare weather across multiple cities
- Calculate average temperature
- Identify the hottest city
- Handle invalid city names
- Command-line interface
- FastAPI API

## Technologies

- Python
- Requests
- FastAPI
- Uvicorn
- Open-Meteo API
- Git & GitHub

## Project Structure

```text
weather/
├── api_client.py
├── weather.py
├── main.py
├── cli.py
├── app.py
├── requirements.txt
└── README.md
Installation
1. Clone the repository
git clone https://github.com/vijaygiri12/api_learning.git
cd api_learning/weather
2. Create a virtual environment
python -m venv .venv
Activate it:
Windows
.venv\Scripts\activate
Linux / macOS
source .venv/bin/activate
3. Install dependencies
pip install -r requirements.txt
Usage
Command-Line Interface
Run:
python cli.py
Available options:
g - Get weather for one city
c - Compare multiple cities
q - Quit
For multiple cities, enter their names separated by commas:
Kolkata,Mumbai,Delhi
FastAPI
Start the server:
uvicorn app:app --host 127.0.0.1 --port 8000
API Endpoints
Single City
GET /weather/{city}
Example:
http://127.0.0.1:8000/weather/Kolkata
Multiple Cities
GET /weather_report/{cities}
Example:
http://127.0.0.1:8000/weather_report/Kolkata,Mumbai,Delhi
Invalid cities are skipped when valid cities are also provided. If no valid cities are found, the API returns 400 Bad Request.
API Documentation
Interactive API documentation is available at:
http://127.0.0.1:8000/docs
Data Source
Weather and geocoding data are provided by the Open-Meteo API.
Stopping the Server
Press:
Ctrl + C
to stop the FastAPI server.
Project Status
This project was built as part of my Python and API development learning journey, covering API integration, HTTP communication, error handling, FastAPI, Git, and GitHub.
'''
