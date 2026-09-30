from api_client import APIClient as Ac

g_client = Ac("https://geocoding-api.open-meteo.com")
f_client = Ac("https://api.open-meteo.com")

def get_weather(city):
    params = {"name": city, "language": "en",
"format": "json"
 }
    result = g_client.get("/v1/search", params=params)
    if result["error"] == False:
        results = result["data"].get("results")
        if not results:
            message = "city " + city + " not found"
            return {"error": True,
    "status_code": result["status_code"],
    "data": message
                }
        else:
            params1 = {"latitude": results[0]["latitude"], 
 "longitude": results[0]["longitude"], 
 "current": "temperature_2m,relative_humidity_2m,wind_speed_10m"}
 
            result1 = f_client.get("/v1/forecast", params=params1)
            
            if not result1["error"]:
                data = result1["data"]["current"]
                data1 = {}
                data1["temperature"] = data["temperature_2m"]
                data1["humidity"] = data["relative_humidity_2m"]
                data1["wind_speed"] = data["wind_speed_10m"]
        
                return {"error": False, 
                "status_code": result1["status_code"],
                "city": city,
                "data": data1
                }
            else:
                return result1
    else:
        return result
        
