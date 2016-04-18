##GPIO Programming with C language on Raspberry Pi 3 using WiringPi library

1.	Assumptions
	- Latest Raspbian and Geany are installed on RPI3

2.	Issues
	- The WiringPi was developed for the previous generation products using BCM8235
	- RPI3 uses BCM8237
	- The documentation for BCM8235 and BCM8237 is not available
	- Potential issues
		a. Are all BCM8235 features binary compatible in BCM8237
		b. Are there useful enhancments in BCM8237 that are not supported by WiringPi

3.	Install GIT Core (used by WiringPi)
	- sudo apt-get install git-core

4.	Install WiringPi
	- git clone git://git.drogon.net/wiringPi

5.	To get an WiringPi update (used at future time)
	- cd wiringPi
	- git pull origin
	- ./build

6.	Add WiringPi library reference in Geany
	- in Raspbian desktop, select Menu, select Programming, select Geany
	- in Geany, select Build, select Set Build Commands
	- in Set Build Commands, append the following string
	
		-lwiringPi
		
	- both to Compile and Build Command strings, such as
	
		gcc -Wall -c "%f" -lwiringPi
		
		gcc -Wall -o "%e" "%f" -lwiringPi
		
	- where
	
		-l is for library reference
		
		wiringPi is the name of the library
		
	- in Set Build Commands, change the Execute command to
	
		sudo "./%e"

7.	Print a reference of RPI3 pin numbers
	- gpio readall

>		+-----+-----+---------+------+---+---Pi 3---+---+------+---------+-----+-----+
>		| BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
>		+-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
>		|     |     |    3.3v |      |   |  1 || 2  |   |      | 5v      |     |     |
>		|   2 |   8 |   SDA.1 |   IN | 1 |  3 || 4  |   |      | 5V      |     |     |
>		|   3 |   9 |   SCL.1 |   IN | 1 |  5 || 6  |   |      | 0v      |     |     |
>		|   4 |   7 | GPIO. 7 |   IN | 1 |  7 || 8  | 1 | ALT5 | TxD     | 15  | 14  |
>		|     |     |      0v |      |   |  9 || 10 | 1 | ALT5 | RxD     | 16  | 15  |
>		|  17 |   0 | GPIO. 0 |   IN | 0 | 11 || 12 | 0 | IN   | GPIO. 1 | 1   | 18  |
>		|  27 |   2 | GPIO. 2 |   IN | 0 | 13 || 14 |   |      | 0v      |     |     |
>		|  22 |   3 | GPIO. 3 |   IN | 0 | 15 || 16 | 0 | IN   | GPIO. 4 | 4   | 23  |
>		|     |     |    3.3v |      |   | 17 || 18 | 0 | IN   | GPIO. 5 | 5   | 24  |
>		|  10 |  12 |    MOSI |   IN | 0 | 19 || 20 |   |      | 0v      |     |     |
>		|   9 |  13 |    MISO |   IN | 0 | 21 || 22 | 0 | IN   | GPIO. 6 | 6   | 25  |
>		|  11 |  14 |    SCLK |   IN | 0 | 23 || 24 | 1 | IN   | CE0     | 10  | 8   |
>		|     |     |      0v |      |   | 25 || 26 | 1 | IN   | CE1     | 11  | 7   |
>		|   0 |  30 |   SDA.0 |   IN | 1 | 27 || 28 | 1 | IN   | SCL.0   | 31  | 1   |
>		|   5 |  21 | GPIO.21 |   IN | 1 | 29 || 30 |   |      | 0v      |     |     |
>		|   6 |  22 | GPIO.22 |   IN | 1 | 31 || 32 | 0 | IN   | GPIO.26 | 26  | 12  |
>		|  13 |  23 | GPIO.23 |   IN | 0 | 33 || 34 |   |      | 0v      |     |     |
>		|  19 |  24 | GPIO.24 |   IN | 0 | 35 || 36 | 0 | IN   | GPIO.27 | 27  | 16  |
>		|  26 |  25 | GPIO.25 |   IN | 0 | 37 || 38 | 0 | IN   | GPIO.28 | 28  | 20  |
>		|     |     |      0v |      |   | 39 || 40 | 0 | IN   | GPIO.29 | 29  | 21  |
>		+-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
>		| BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
>		+-----+-----+---------+------+---+---Pi 3---+---+------+---------+-----+-----+

8.	Run Hello World in Geany
	- enter the following text and save it as hello.c

>     #include <stdio.h>

>     int main() {
> 	    printf("Hello my World\n");
> 	    return 0;
>     }

	- press F8 to compile the text
	- press F9 to build executable file
	- press F5 to start execution
	- in the LXTerminal, press return to close the dialog

9.	Blink an external LED
	- connect a LED and a resistor (0.22 - 1.0 k) between GPIO23 and GND
	- enter the following text and save it as blink.c
	
>		#include <stdio.h>
>		#include <wiringPi.h>
>
>		// LED Pin - wiringPi pin 4 is physical pin 16, BCM pin GPIO 23
>
>		#define LED     4
>
>		int main (void) {
>		  printf ("Raspberry Pi blink\n") ;
>
>		  wiringPiSetup ();
>		  pinMode (LED, OUTPUT) ;
>
>		  for (;;) {
>		    digitalWrite (LED, HIGH);   // On
>		    delay (500) ;               // mS
>		    digitalWrite (LED, LOW);    // Off
>		    delay (500) ;
>		  }
>		  return 0;
>		}

	- press F8 to compile the text
	- press F9 to build executable file
	- press F5 to start execution
	- in the LXTerminal, press Ctrl-C to break the infinite loop
