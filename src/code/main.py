def main():
	import os, sys, time
	import json, platform

		
	if platform.system() == "linux" or "darwin":  # linux, darwin == macos
		clear_cmd = "clear"
	else:
		clear_cmd = "cls"
	os.system(clear_cmd)

	with open("DEV.json", "r") as DEVFile:
					# understand data (again sadly ;-;)
					data = DEVFile.read()
					# parse file (sigh)
					obj = json.loads(data)
					developer_username = str(obj['DEVELOPER_USERNAME'])
					application_version = str(obj['APPLICATION_VERSION'])

	print(f"""(WEATHR BY '{developer_username}')
	(VERS.  {application_version})


		Start     //  1
		Info      //  2
		Exit App  //  3
	""")
	main_page_choice = str(input("User_Input://   "))
	os.system(clear_cmd)

	def menu():
		if main_page_choice == "1":

			installDependancies = str(input(f"""(WEATHR BY '{developer_username}')
		(VERS.  {application_version})
		Install The Dependancies?

			Yes       //  1
			No        //  2
			Exit App  //  3			    

		User_Input://   """))

			if installDependancies == "1":
				print("Installing dependencies.. \nPlease wait..")
				os.system("pip3 install --upgrade pip")
				os.system("pip3 install -r needs.txt --upgrade")
				os.system(clear_cmd)

				print("Done, press enter to start the script.")
				input()
				os.system(clear_cmd)
				from code.weather import get_weather
				get_weather()

			elif installDependancies == "2":
				print("Running script...")
				os.system(clear_cmd)
				from code.weather import get_weather
				get_weather()
			
			elif main_page_choice == "3":
				print("User Exited Application.")
				sys.exit(0)

			elif main_page_choice != "1" or "2" or "3":
				os.system(clear_cmd)
				print("Invalid Input. Quiting..")
				sys.exit()

		elif main_page_choice == "2":
			from code.info import display_info
			display_info()

		elif main_page_choice == "3":
			sys.exit(0)

		else:
			os.system(clear_cmd)
			print("Invalid Input.")
			time.sleep(2)
			menu()

