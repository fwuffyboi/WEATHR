import os, sys, platform

# print("Installing dependencies.. \nPlease wait..")
# os.system("pip3 install --upgrade pip")
# os.system("pip3 install geocoder --upgrade")
# os.system("pip3 install requests --upgrade")


import geocoder, requests
import time, string

print("Getting OS..")
print(platform.system())
os_platform = platform.system()

if platform.system() == "linux" or "darwin":  # linux, darwin == macos
    clear_cmd = "clear"
else:
    clear_cmd = "cls"

os.system(clear_cmd)

print("Getting Location..")

# grabs the user's general location in coordinates.
ip_info_addr = requests.get("https://ipinfo.io/json")
ip_address = ip_info_addr.json()['ip']

location = geocoder.ip(ip_address)
# print(geocoder.ip('me'))
location_lat = location.lat
location_lng = location.lng


def get_weather():
    while True:
        os.system(clear_cmd)
        print("PLEASE WAIT, GETTING DATA.")

        # api key for retrieving the weather
        api_key = open("api_key.txt", "r")
        api_key = str(api_key.readline())
        print(api_key)
        lang = 'en'

        # requests for the weather.
        final_url = f'http://api.openweathermap.org/data/2.5/weather?appid={api_key}&lat={str(location_lat)}&lon=' \
                    f'{str(location_lng)}&lang={lang}&units=metric'

        # turning weather json data into a dict.
        weather_data = (requests.get(final_url).json())
        print(weather_data)
        if weather_data['cod'] == 401:
            os.system(clear_cmd)
            print(f"CRITICAL_ALERT://   {weather_data['message']}")
            print(f"\n\nThe tested API key is '{api_key}'.")
            exit()

        # displaying data needed.
        weather_main = weather_data['weather'][0]['main']
        weather_desc = weather_data['weather'][0]['description']
        temp = weather_data['main']['temp']
        wind_speed = weather_data['wind']['speed']
        humidity = weather_data['main']['humidity']
        air_pressure = weather_data['main']['pressure']
        latitude = weather_data['coord']['lat']
        longitude = weather_data['coord']['lon']
        icon_id = weather_data['weather'][0]['icon']

        # prints whole json api output.
        # print(weather)

        weather_printed = (f"""(Weather:  {weather_main})
    (Description: {string.capwords(weather_desc)})
    (Temperature:  {temp} °C)
    (Wind Speed:  {wind_speed} mph)
    (Humidity:  {humidity} %)
    (Air Pressure:  {air_pressure} inHg)
(Location:   )
    (Estimated Latitude:  {latitude})
    (Estimated Longitude:  {longitude})""")

        wait_time = 60  # time to wait between every request for weather.
        # limit is 1 request per second with a free account.

        for i in range(wait_time):
            os.system(clear_cmd)
            wait_time -= 1
            print(weather_printed)
            print(f"\n\nRefreshing in://  {wait_time}")
            time.sleep(1)


get_weather()
