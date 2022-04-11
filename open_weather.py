import requests
from pprint import pprint

open_weather_key = 'dbe1cd97e40547c2cf836a3465e37857'

def get_weather(city, API):
    r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid="
                 f"{API}&units=metric")
    data = r.json()
    pprint(f"""Название города: {(data['name'])}
    Температура: {data['main']['temp']}
    Влажность: {data['main']['humidity']}
    Давление: {data['main']['pressure']}
    Уровень моря: {data['main']['sea_level']}
    """)

def main():
    city = input("Введите название города: ")
    get_weather(city, open_weather_key)

if __name__=='__main__':
    main()
