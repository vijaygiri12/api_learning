from fastapi import FastAPI, HTTPException
from weather import get_weather
from main import compare_weather
app = FastAPI()

@app.get("/weather/{city}")
def weather(city: str):
    report = get_weather(city.strip().capitalize())
    if report["error"]:
        raise HTTPException(status_code=404, detail=report["data"])
    return report

@app.get("/weather_report/{cities}")
def weather_report(cities: str):
    city_list = [city.strip() for city in cities.split(',') if city.strip()]
    if not city_list:
        raise HTTPException(
            status_code=400,
            detail="No cities were provided."
        )

    result = compare_weather(city_list)

    if result is None:
        raise HTTPException(
            status_code=404,
            detail="No valid cities were found."
        )

    return result
