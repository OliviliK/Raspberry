# Raspberry
##Raspberry Pi usage in robotics
###RPI 3 for camera interface and robot management
###RPI 0 for sensor and actuator interface

##Issues
###Voltage levels
Many sensors and actuators are using 5V logic and all RPI I/O uses 3.3V.

##Benefits
###RPI 3 has built-in WiFi connection
The headless development is really nice.
###RPI 0 is very low cost
The low price ($5) has created an inbalance between suply and demand.
For this reason, RPI 0 is not available for purchases.
The total cost with level shifters and other missing features is quite high.

##Alternatives
The new ESP32 has built-in WiFi and quite high performance and very low price ($4).
It is based on the experience that Espressif has learned with ESP8266.  The ESP8266 has wide support for robotics type of applications.
