import os, time, string, subprocess
f = open("WEATHR_CONF.txt", "w+")

try:
    settings_file = open("WEATHR_CONF.txt", "w+")
    if settings_file.read(1) == "":
        os.system("clear")
        input("You don't seem to have the settings set-up, lets do that!\nPress {enter} key to continue.")
        os.system("clear")

        lang = "en"  # we only support english
        def get_units():
            units = input("Would you prefer Metric (°C) or Imperial (°F) units?\nType (M) for metric and (I) for imperial!\n")
            if units == "M" or "I":
                if units == "M":
                    units = "metric"
                else:
                    units = "imperial"

                return units

            else:
                get_units()

        get_units()

        # getting custom lat/lon

        os.system("clear")
        print("Would you like to add a custom Latitude/Longitude?\nIf so, type in your latitude. If not, press enter.\n")
        lat = input()

        if lat == "":
            pass
        else:
            print("Enter your Longitude:\n")
            lon = input()

        # getting api key

        os.system("clear")
        print("FINALLY! What is your api key? (so we can get the weather..)\n")
        api_key = input()
        os.system("clear")
        

        settings = f"""{lang}
{units}
{lat}
{lon}
{api_key}"""
        print(settings)
        time.sleep(10)
        print("Saving file..")
        settings_file.close()
        print("Saved!")
        os.system("clear")
        print("Done, installing packages..")
        os.system("pip3 install --upgrade pip && pip3 install geocoder --upgrade && pip3 install requests --upgrade")



    else:
        pass


except: # Exception as e:
    #print(f"CRITICAL_ERROR://   {e}")
    #exit()
    pass


import geocoder, requests
g = geocoder.ipinfo("me")


os.system("clear")
print("Getting Location..")


def get_weather():
    # if file exists, get settings and apply them

    lang = settings_file.read(1)
    units = settings_file.read(2)
    lat = settings_file.read(3)
    lon = settings_file.read(4)
    api_key = settings_file.read(5)


    while True:
        os.system("clear")
        
        print("PLEASE WAIT, GETTING LOCATION.")
        # grabs the user's general location in coordinates.
        ipinfo_addr = requests.get("https://ipinfo.io/json")
        # ip_address = ipinfo_addr.json()['ip']
        ip_address = g.ip
        location = geocoder.ip(ip_address)
        # print(geocoder.ip('me'))

        if lat == "" and lon == "":
            location_lat = location.lat
            location_lng = location.lng

        else:
            location_lat = lat
            location_lon = lon

        print("PLEASE WAIT, zxGETTING DATA.")

        # api key for retrieving the weather
        API_key = api_key  # "8a6e896725fa8e323bf8352cf8fad381"
        lang = lang

        # requests for the weather.
        Final_url = f'http://api.openweathermap.org/data/2.5/weather?appid={API_key}&lat={str(location_lat)}&lon={str(location_lng)}&lang={lang}&units={units}'

        # turning weather json data into a dict.
        weather_data = (requests.get(Final_url).json())

        # displaying data needed.
        weather_main = weather_data['weather'][0]['description']
        temp = weather_data['main']['temp']
        wind_speed = weather_data['wind']['speed']
        humidity = weather_data['main']['humidity']
        air_pressure = weather_data['main']['pressure']
        latitude = weather_data['coord']['lat']
        longitude = weather_data['coord']['lon']

        # this is to censor the ip for privacy reasons. (duh.) btw pass the var as the ip address var.
        for num in ip_address:
            if num.isdigit():
                ip_address = ip_address.replace(num, "*")

        # prints whole json api output.
        # print(weather)

        weather_printed = (f"""(Weather:  {string.capwords(weather_main)})
    (Temperature:  {temp} °C)
    (Wind Speed:  {wind_speed} mph)
    (Humidity:  {humidity} %)
    (Air Pressure:  {air_pressure} )
    (Estimated Latitude:  {latitude})
    (Estimated Longitude:  {longitude})
    (IP_Address:  {ip_address})""")

        wait_time = 10
        for i in range(wait_time):
            wait_time -= 1
            os.system("clear")
            print(weather_printed)
            print(f"\n\nRefreshing in://  {wait_time}")
            time.sleep(1)


get_weather()
