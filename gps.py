#Author:Rucha Chauthai
#inteface GPS device SIM28L with raspberry pi

#Activate UART protocol from 
#Raspberry menu -> preferences -> Raspberry pi configuration ->
#		->interfaces -> serial port=enable, serial console= disable

#pin connections
#5V to pin 4
#GND to pin 6
#Tx to pin 10

import serial							#pyserial library for UART

#an object with name gps, COM port as serial0, 9600 baud rate 
#COM port can be seen with command "ls /dev"
#for USB port use ttyUSB0 or its number

gps = serial.Serial("/dev/serial0", 9600)

try:									#read port
	while True:
		x=port.readline()			#reads untiil a \n is found
		data=x.split(",")

		if data[0]=="$GPRMC" and data[2]=="A" :
			lat = int(data[3][0:2]) + float(data[3][2:])/60
			lon = int(data[5][0:3]) + float(data[5][3:])/60

		print "Latitude: ", lat
		print "Longitude: ", lon

except KeyboardInterrupt :		#if CTRL+C is pressed
	port.close()				#close the open port
	del port					#delete the port object