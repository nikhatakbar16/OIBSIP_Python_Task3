import requests
import json
from datetime import datetime

class WeatherApp:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    def get_weather(self, city_name):
        params = {
            'q': city_name,
            'appid': self.api_key,
            'units': 'metric' 
        }
        
        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching weather data: {e}")
            return None
    
    def display_weather(self, weather_data):
        if not weather_data:
            print("No weather data available.")
            return
        
        if weather_data.get('cod') != 200:
            print(f"Error: {weather_data.get('message', 'Unknown error')}")
            return
        
        city = weather_data['name']
        country = weather_data['sys']['country']
        temp = weather_data['main']['temp']
        feels_like = weather_data['main']['feels_like']
        humidity = weather_data['main']['humidity']
        pressure = weather_data['main']['pressure']
        weather_desc = weather_data['weather'][0]['description'].title()
        wind_speed = weather_data['wind']['speed']
        
        
        print("\n" + "="*50)
        print(f"WEATHER FORECAST - {city}, {country}")
        print("="*50)
        print(f"🌡️  Temperature: {temp}°C (Feels like: {feels_like}°C)")
        print(f"☁️  Conditions: {weather_desc}")
        print(f"💧 Humidity: {humidity}%")
        print(f"📊 Pressure: {pressure} hPa")
        print(f"💨 Wind Speed: {wind_speed} m/s")
        print("="*50)
    
    def run(self):
        print("🌤️  Welcome to Python Weather App! 🌤️")
        print("Type 'quit' to exit the app\n")
        
        while True:
            city = input("Enter city name: ").strip()
            
            if city.lower() == 'quit':
                print("Thank you for using the Weather App! 👋")
                break
            
            if not city:
                print("Please enter a valid city name.")
                continue
            
            print(f"\nFetching weather data for {city}...")
            weather_data = self.get_weather(city)
            self.display_weather(weather_data)
API_KEY = "1a8b9f5cd277773d22d8acbf2c30e50e"

app = WeatherApp(API_KEY)
app.run()