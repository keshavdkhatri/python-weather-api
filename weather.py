import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")


BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")

params = {
  "q":city,
  "appid":API_KEY,
  "units":"metric"
}

try:
    response = requests.get(BASE_URL,params=params)

    if response.status_code == 200:
        data = response.json()

        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]


        print(f"\n---- Weather in {city.title()} ----")
        print(f"Temperature: {temperature}°C")
        print(f"Condition: {description.capitalize()}")
        print(f"Humidity: {humidity}%")

    else:
        print(f"\nError: Could not find city '{city}'. Please check the spelling.")

except requests.exceptions.RequestException as e:
    print(f"\nAn error occured while connecting to the API: {e}")