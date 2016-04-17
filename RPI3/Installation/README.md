#Raspberry Pi 3 installation steps
##Tools used
- Micro SD Card formatter
- Raspbian Jessie
- Win32 Disk Imager
- Kitty terminal
- XDRP remote desktop
- Geany editor
- Python Interpreter

###1. Download and install SD Formatter for Windows
	- https://www.sdcard.org/downloads/formatter_4

###2. Insert a 16 or 32 GB Micro SD card and format it with SDFormatter

###3. Download latest Raspbian Jessie, such as 2016-03-18-raspbian-jessie
	- https://www.raspberrypi.org/downloads/raspbian/

###4. Extract the 2016-03-18-raspbian-jessie.img by moving it out from
	- 2016-03-18-raspbian-jessie.zip
	- in downloads directory

###5. Download and install Win32 Disk Imager
	- https://sourceforge.net/projects/win32diskimager/

###6. Run Win32Diskimager
	- Select the 2016-03-18-raspbian-jessie.img in download directory
	- Select the drive with formatted Micro SD card
	- Start imaging, this takes few minutes

###7. Download KiTTY telnet/SSH client
	- http://www.9bis.net/kitty/

###8. Move kitty.exe from download folder to a more permanent folder
	- such as C:Users\<user>\Documents\LocalApps

###9. Prepare RPI3
	- move the SD card from PC into RPI3
	- connect Ethernet cable to RPI3
	- connect USB cable to RPI3 for power (5V 2A)

###10. Find the RPI3 IP and MAC address
	- use a tool, such as Fing
	- write them down, such as 
		192.168.1.37 b8:27:eb:28:19:fc for wired connection
		192.168.1.38 b8:27:eb:7d:4c:a9 for WiFi

###11. Start KiTTY
	- enter the wired IP address as Host Name
	- click Open

###12. In the SSH session
	- enter pi as login ID
	- enter raspberry as password
	- find the available network names
		sudo iwlist wlan0 scan | grep ESSID

###13. If MAC address based network security is required,
	- add the WiFi MAC to the enabled list
	- write down the network password

###14. Edit network setup file with nano editor
	- sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
	- on first line change country from GB to US (or whatever is your country ID)
	- append the following lines

		network={
		    ssid="Selected network name"
		    psk="Network password"
		}

	- WriteOut file with Ctrl-O
	- Exit with Ctrl-X

###13. Shutdow RPI3 and prepare for WiFi
	- sudo shutdown
	- after 1 minute, when the shutdown is complete
		disconnect Ethernet cable
		disconne USB power source

###14. Reboot RPI13 by reconnecting USB power

###15. Start Kitty and login
	- use the WiFi IP addres as the Host name
	- login as pi with raspberry as password

###16. Install Remote Desktop, XDRP
	- sudo apt-get install xrdp
	- confirm, with Y, that the additional space usage is OK
	- this takes few minutes
	- sudo reboot

###17. Start Remote Desktop Connection
	- enter WiFi IP address as Computer name
	- confirm that you want to connect to an unidentified computer
	- in the XRDP logon dialog,
		enter pi as username
		enter raspberry as password
	- check the RPI3 desktop by starting Epiphany web browser (2nd icon in menu bar)
	- enter google.com as URL
	- open Terminal (4th icon in menu bar)
	- in Terminal command line, shutdown RPI3
		sudo shutdown
	- after 1 minute, when the shutdown is complete
		disconnect USB power source
		move the CD card back to PC

###18. Make a backup copy of the image
	- Start Win32Diskimager
	- Enter the image name, by browsing into target location
	- Click Read button
	- this takes several minutes

###19. Restart RPI
	- move the CD card back into RPI
	- reconnect USB power
	- open Remote Desktop Connection

###20. Download and install Geany editor
	- open Terminal
	- sudo apt-get install geany
	- confirm that additional space usage is OK

###21. Start Geany for first Python program
	- open main menu (1st icon in menu bar)
	- select programming
	- select Geany
	- select tab untitled - Geany
	- enter the following text
		print "RPI3 greets the World"
	- save the file with Ctrl-S
		select pi folder
		click Create Folder button
		enter myPython as folder name
		enter helloWorld.py as file name
	- in Terminal command line, write
		python myPython/helloWorld.py
	- observe the text after the command
		RPI3 greets the World

###22. Create Python program with physical I/O
	- connect CanaKit Raspberry Pi GPIO Breakout Board or similar board to RPI3
	- connect Canakit to a breadboard
	- insert an infrared collision detection sensor or similar to breadboard
		- when the sensor pins are in order OUT, GND, VCC
		  the sensor can use GPIO 14 in pin 8
	- in other words, the sensor pins are connected without any wires
		- OUT to pin 8
		- GND to pin 6
		- VCC to pin 4
	- using Geany, create the following file myPython/helloSensor.py

		import RPi.GPIO	as GPIO			## Import GPIO Library
		import time				## Import 'time' library (for 'sleep')
		 
		pin = 8					## Sensor connected to pin 8
		GPIO.setmode(GPIO.BOARD)		## Use BOARD pin numbering
		GPIO.setup(pin,	GPIO.IN)		## Set pin 8 to	INPUT

		prevState = GPIO.input(pin)		## Save	the current pin	state
		prevTime = time.time()			## Store the starting time
		 
		while True:				## Do this forever
			newState = GPIO.input(pin)	## Read sensor state
			if newState <> prevState:	## Detect change in sensor state
				newTime = time.time()	## Record the change time
				duration = newTime - prevTime
							## Show the result
				print "State {: d} lasted {: 6.1f} ms".format(prevState, duration * 1000)
				prevState = newState	## save state value
				prevTime = newTime	## save time value
			time.sleep(0.001)		## wait 1 ms between readings
		 
		GPIO.cleanup()				## Cleanup

###23. Run helloSensor.py
	- python myPython/helloSensor
	- activate the sensor with rapid moves
	- observe the recorded sensor readings with 0.1 ms resolution
	- stop the readings with Ctrl-C


