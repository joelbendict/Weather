import requests

API_KEY = "**************"  # Replace with your actual OpenWeather API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    return data

def display_weather(weather_data):
    if weather_data.get("cod") == 200:
        temperature = weather_data["main"]["temp"]
        description = weather_data["weather"][0]["description"]
        print(f"Weather: {description}")
        print(f"Temperature: {temperature}°C")
    elif weather_data.get("cod") == "404":
        print("City not found.")
    else:
        print("Unable to fetch weather data.")

def main():
    city = input("Enter city name: ")
    weather_data = get_weather(city)
    display_weather(weather_data)

if __name__ == "__main__":
    main()
