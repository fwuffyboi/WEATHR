import geocoder, requests
import platform, os
import time, string
import json, sys


def get_weather():
    print("Running Script.")

    print("Getting OS..")
    print(platform.system())

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

    def get_weather_two():
        while True:
            os.system(clear_cmd)
            print("PLEASE WAIT, GETTING DATA.")

            with open('settings.json', 'r') as settingsFile:
                # understand data (bruh)
                data = settingsFile.read()
                # parse file
                obj = json.loads(data)

                # get values
                # getting api key
                print("Api Key://  " + "*" * len(str(obj['api_key'])))
                api_key = str(obj['api_key'])

                # getting language (english obvs but yknow. we need it for api requests ;-;)
                print("Language://  " + str(obj['language']))
                lang = str(obj['language'])

                # getting request refresh time.
                print("Request Refresh Time (in seconds)://  " + str(obj['refresh_time']))
                wait_time = int(obj['refresh_time'])

            with open("DEV.json", "r") as DEVFile:
                # understand data (again sadly ;-;)
                data = DEVFile.read()
                # parse file (sigh)
                obj = json.loads(data)

                # get values
                # getting developer name (duh)
                print("Developer Username://  " + str(obj['DEVELOPER_USERNAME']))
                developer_username = str(obj['DEVELOPER_USERNAME'])

                # get app version
                print("Application Version://  " + str(obj['APPLICATION_VERSION']))
                application_version = str(obj['APPLICATION_VERSION'])

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
                sys.exit()

            # displaying data needed.
            weather_main = weather_data['weather'][0]['main']
            weather_desc = weather_data['weather'][0]['description']
            temp = weather_data['main']['temp']
            wind_speed = weather_data['wind']['speed']
            humidity = weather_data['main']['humidity']
            air_pressure = weather_data['main']['pressure']
            latitude = weather_data['coord']['lat']
            longitude = weather_data['coord']['lon']
            sunrise = weather_data['sys']['sunrise']
            sunset = weather_data['sys']['sunset']
            icon_id = weather_data['weather'][0]['icon']

            # prints whole json api output.
            # print(weather)

            weather_printed = (f"""

(WEATHR BY '{developer_username}')
(VERS. {application_version})

    (Weather:  {weather_main})
            (Description: {string.capwords(weather_desc)})
            (Temperature:  {temp} °C)
            (Wind Speed:  {wind_speed} mph)
            (Humidity:  {humidity} %)
            (Air Pressure:  {air_pressure} inHg)
    (Location:   
            (Estimated Latitude:  {latitude})
            (Estimated Longitude:  {longitude})
    (Solar:  
	    (Current Time: {str(time.strftime("%H:%M:%S", time.gmtime(time.time())))})
            (Sunrise:  {str(time.strftime("%H:%M", time.gmtime(sunrise)))})
            (Sunset:  {str(time.strftime("%H:%M", time.gmtime(sunset)))})
""")

            for i in range(wait_time):
                os.system(clear_cmd)
                wait_time -= 1
                print(weather_printed)
                print(f"\n\nRefreshing in://  {wait_time}")
                time.sleep(1)

    get_weather_two()
