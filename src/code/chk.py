def chk():
    # checking imports work.
    try:
        import PIL
        import PySimpleGUI
        import geocoder
        import requests
        import os, sys, json

    except ImportError as err:
        print(f"ERR:// Packages not installed. "
              f"To continue, please install all required packages listed in the 'requirements' file. "
              f"errCode:// {err}")
        sys.exit(f"ERR:// Packages not installed. "
                 f"To continue, please install all required packages listed in the 'requirements' file. "
                 f"errCode:// {err}")

    except Exception as err:
        print(f"ERR:// Unknown error. "
              f"errCode:// {err}")
        sys.exit(f"ERR:// Unknown error. "
                 f"errCode:// {err}")

    finally:
        # checking API keys.
        try:
            with open('../settings.json', 'r') as settingsFile:
                # understand data
                data = settingsFile.read()

                # parse file
                obj = json.loads(data)
                print("Api Key://  " + "*" * len(str(obj['owm_api_key'])))
                api_key = str(obj['owm_api_key'])

            final_url = f'http://api.openweathermap.org/data/2.5/weather?appid={api_key}'

            weather_data = (requests.get(final_url).json())
            # print(weather_data)
            if weather_data['cod'] == 401:
                print(f"ERR://   {weather_data['message']}")
                print(f"\n\nThe tested API key is '{api_key}'.")

            elif weather_data['cod'] == 400:
                print("Your API key is working fine!")
                print(f"\n\nThe tested API key is '{api_key}'.")

        except Exception as err:
            print(f"ERR:// Unknown error. "
                  f"errCode:// {err}")
            sys.exit(f"ERR:// Unknown error. "
                     f"errCode:// {err}")

        finally:
            return "chk pass"


chk()
