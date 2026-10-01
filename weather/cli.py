from main import get_single_city_report, compare_weather
import json
from pathlib import Path

folder = Path(__file__).resolve().parent / "data"
folder.mkdir(exist_ok=True)

file_path = folder / "weather.json"
while True:
    
    print("(This program gives weather update for given city name)")
    print("(what do you want to do? \nget report about one city or compare multiple cities)")
    print("(Enter 'q' to quit or 'g' to get report or 'c' to compare)")
    prompt = ("please enter you query: ")
    query = input(prompt)
    if query.lower() == "q":
        break
        
    elif query.lower() == "g":
        name = input("enter city name: ")
        if not name:
            print("please enter city name")
        else:
            city = get_single_city_report(name)
            print(city)
        
    elif query.lower() == "c":
        prompt = (" enter cities names separated with , : ")
        city = input(prompt)
        city_list = (city)
        cities_list = [city.strip() for city in city_list.split(",") if city.strip() ]
        
        print("getting data from server")
        result = compare_weather(cities_list)
        print(result)
        if not result["success"]:
            pass
        else:
            with open(file_path, "w") as file:
                json.dump(result, file, indent=4)
                print("file is saved here: ", file_path)
    else:
        print("invalid input")
        continue
        
        
