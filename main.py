import os, sys
import json, platform
from weather import get_weather


print("Getting OS..")
print(platform.system())
os_platform = platform.system()
	
if platform.system() == "linux" or "darwin":  # linux, darwin == macos
	clear_cmd = "clear"
else:
	clear_cmd = "cls"
os.system(clear_cmd)

	
print("Install The Dependancies?")
installDependancies = str(input("""
Yes  //  1
No   //  2			    

User_Input://   """))

if installDependancies == "1":
	print("Installing dependencies.. \nPlease wait..")
	os.system("pip3 install --upgrade pip")
	os.system("pip3 install -r needs.txt --upgrade")
	os.system(clear_cmd)

	print("Done, press enter to start the script.")
	input()
	os.system(clear_cmd)

	get_weather()

elif installDependancies == "2":
	print("NOT installing dependancies.")
	print("Done, running script.")
	os.system(clear_cmd)

	get_weather()

else:
	os.system(clear_cmd)
	print("Invalid Input. Quiting..")
	sys.exit()
