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
