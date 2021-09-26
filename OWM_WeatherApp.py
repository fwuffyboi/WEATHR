import os, sys, platform


print("Installing dependencies.. \nPlease wait..")
os.system("pip3 install --upgrade pip")
os.system("pip3 install geocoder --upgrade")
os.system("pip3 install requests --upgrade")


import geocoder, requests
import time, string

print("Getting OS..")
print(platform.system())
os_platform = platform.system()

if platform.system() == "linux":  # linux ofc
    clear_cmd = "clear"
elif platform.system() == "darwin":  # mac os
    clear_cmd = "clear"
elif platform.system() == "Windows":  # wondows lol
    clear_cmd = "cls"
else:
    clear_cmd = ""  # if undefined then nothing.

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
        api_key = os.environ['API_KEY.env']
        lang = 'en'

        # requests for the weather.
        final_url = f'http://api.openweathermap.org/data/2.5/weather?appid={api_key}&lat={str(location_lat)}&lon=' \
                    f'{str(location_lng)}&lang={lang}&units=metric'

        # turning weather json data into a dict.
        weather_data = (requests.get(final_url).json())
        print(weather_data)
        if weather_data['cod'] == 401:
            print("CRITICAL_ALERT://   Invalid API key. For more information, visit "
                  "'http://openweathermap.org/faq#error401'")
            sys.exit(2)

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

        weather_printed = (f"""(Weather:  {string.capwords(weather_main)})
    (Description: {string.capwords(weather_desc)})
    (Temperature:  {temp} °C)
    (Wind Speed:  {wind_speed} mph)
    (Humidity:  {humidity} %)
    (Air Pressure:  {air_pressure} inHg)
    (Estimated Latitude:  {latitude})
    (Estimated Longitude:  {longitude})
    (Icon_ID: {icon_id})""")

        wait_time = 20
        half_wt = int(wait_time / 2)
        print(half_wt)

        for i in range(wait_time * half_wt):
            wait_time -= 0.1
            # print("WEATHER")
            print(f"\n\nRefreshing in://  {wait_time}")
            time.sleep(0.1)
            if wait_time < 0:
                break


get_weather()
