from fastapi import FastAPI, HTTPException
from weather import get_weather

app = FastAPI()

@app.get("/weather")
def weather(city):
    report = get_weather(city.strip().capitalize())
    if report["error"]:
        raise HTTPException(status_code=404, detail=report["data"])
    return report
