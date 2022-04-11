import requests
from pprint import pprint

open_weather_key = 'dbe1cd97e40547c2cf836a3465e37857'

city = input("Введите название города: ")

r = requests.get(f"https://api.openweathermap.org/data/2.5/"
                 f"weather?q={city}&appid={open_weather_key}&units=metric")
data = r.json()
#pprint(data)
pprint(data['name'])
pprint(data['coord'])
pprint(data['sys']['country'])
pprint(data['main'])

