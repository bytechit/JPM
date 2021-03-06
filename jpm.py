#!/usr/bin/python3
import sys
import os
import shutil

def jpminstall(p, n, pn, icon):
	os.system("clear")
	print("Package Manager 1.0")
	if '.deb' in p or '.DEB' in p:
		if os.path.isfile(p):
			os.system("sudo dpkg -i " + os.path.join(p) + " || echo \"Error, the Debian application hasn't been installed\" && exit")
			os.system("sudo apt update")
			print("The Debian application has been correctly installed.")
			exit()
	if '.AppImage' in p or '.APPIMAGE' in p or '.appimage' in p:
				
		#Get name
		n = p.lower().replace(".appimage", "")
		pn = p.replace(".AppImage", "")
		icon=""

		#Get real name

		print("Application Name is: " + pn + ". Is that name correct? (y or n)")
		x = input()
		if (x.lower() == "n"):
			print("Insert a name for the application: ")
			n = input()
			print("Insert a pretty name for the application: ")
			pn = input()
		elif (x.lower() == "y"):
			pass
		else:
			print("Command not recognized. Abort.")
			exit()

		#move

		try:
			shutil.move(os.path.join(p), "/usr/bin/"+ n.lower())
			os.system("chmod +x /usr/bin/"+n)
		except:
			print("Error during the moving.")
		#icon
		print("Creating .desktop file")
		f = open("/usr/share/applications/"+ n + ".desktop","w")
		f.write("""[Desktop Entry]
Type=Application
Name={}
Exec=/usr/bin/{}
Icon={}
Terminal=False
		""".format(pn, n, icon))
		print("Installation completed!")
		exit()

if os.geteuid() != 0:
    exit("You need to have root privileges to run JPM.\nPlease try again, this time using 'sudo'. Exiting.")

if sys.argv[1:]:
	if sys.argv[1] == "--help"  or sys.argv[1] == "-h":
		print("Welcome to Jonio Pack Manager")
		print("jpm [APPNAME].deb	To Install a Debian package.")
		print("jpm [APPNAME].AppImage	To Install a file AppImage.")
		print("jpm [APPNAME] -n [BIN_NAME] -pn [PRETTY_NAME] -i [ICON_PATH]	To install an AppImage file full of pretty name and icon")
		exit()
	elif sys.argv[1] == '-v' or sys.argv[1] == '--version':
		print("1.0")
		exit()
	else:
		try:
			jpminstall(sys.argv[1],"","","")
		except:
			print("Bad format.")
			exit()

if sys.argv[7:]: # jpm APP -n NAME -pn PRETTYNAME -i ICON
	try:
		jpminstall(sys.argv[1],sys.argv[3],sys.argv[5],sys.argv[7])
	except:
		print("Bad format.")
		exit()
	



print("No args detected. Type jpm --help.")
exit()