#  Simple Weather App in Python


import requests

#  OpenWeatherMap API Key here
API_KEY = "YOUR_API_KEY_HERE"

# 1 Ask user for city name
city = input("Enter city name: ")

# Create API URL
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

try:
    #  Send request to weather server
    response = requests.get(url)

    #  Convert response into JSON format (Python dictionary)
    data = response.json()

    #  Check for errors (invalid city or API issue)
    if response.status_code != 200:
        print(" Error: Invalid city name or API problem.")
    else:
        #  Extract weather details
        temp_kelvin = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"]
        wind_speed = data["wind"]["speed"]

        #  Convert temperature
        temp_celsius = temp_kelvin - 273.15
        temp_fahrenheit = (temp_celsius * 9/5) + 32

        #  Display output
        print("\n🌍 Weather Report")
        print("City:", city)
        print(f"Temperature: {temp_celsius:.2f}°C / {temp_fahrenheit:.2f}°F")
        print("Condition:", condition)
        print("Humidity:", humidity, "%")
        print("Wind Speed:", wind_speed, "m/s")

#  Error handling
except requests.exceptions.ConnectionError:
    print(" No internet connection!")
except Exception as e:
    print(" Something went wrong:", e)

