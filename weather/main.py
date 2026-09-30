from weather import get_weather

def get_single_city_report(city):
    
    city_name = city.lower()
    city_name1 = city_name.capitalize()
    print("getting data for city", city)
    report = get_weather(city_name1)
    if report["error"]:
        return report["data"]
    else:
        return report
    
def compare_weather(cities_list):
    weather_data = []
    cities_names = []
    temps = []
    
    if not cities_list:
        return "the list was empty."
    else:
            city_list = []
            for city in cities_list:
                    city_list.append(city.capitalize())
            city_names = list(dict.fromkeys(city_list))        
            for city in city_names:
                    print("getting data for city, ", city)
                    result = get_weather(city)
                    if result["error"]:
                        print(result["data"])
                        continue
                    else:
                        print("appending data for, ", city)
                        cities_names.append(city)
                        weather_data.append(result)
                        temps.append(result["data"]["temperature"])
            
    
    
    if temps != []:
        
        avg_temp = round(sum(temps)/len(cities_names),1)
        max_temp = max(temps)
        max_index = temps.index(max_temp)
        hottest_city = cities_names[max_index]
        result1 = {}
        result1["Average_temperature"] = avg_temp
        result1["hottest_city"] = hottest_city
        result1["highest_temperature"] = max_temp
        result1["weather_data"] = weather_data
        return result1
