#Author: Rucha Chauthai
#pin connections
#ultrasonic VCC pin 4 and GND to pin 6
#trigger pin 40
#echo pin 38

from RPi import GPIO as g 			#import GPIO class from RRPi module
import time							#time module for delays

trigger = 40						#defined trigger pin number
echo = 38							#defined echo pin number

g.setmode(g.BOARD)					#setting the pin number to board mode
g.setwarnings(False)				#warnings false
g.setup(trigger, g.OUT)				#led pin as output
g.setup(echo, g.IN)					#switch pin as input

g.output(trigger, False)			#initially setting trigger pin low

try:

	while True:						#forever
		
		g.output(trigger,  True)	#generate pulse of 10 us to initiate reading
		time.sleep(0.000001)
		g.output(trigger,False)

		while g.input(echo)==0:		#wait for pin to go HIGH
			start=time.time()		#keep rolling until the HIGH edge is found

		while g.input(echo)==1:		#wait for pin to go LOW
			stop = time.time()		#keep rolling until the HIGH edge is found

		elapsed = stop-start		#find time between events
		distance = 34300*elapsed/2	#distance = speed x time / 2 

		print distance				#print value of distance
		time.sleep(1)

except KeyboardInterrupt :		#if CTRL+C is pressed
	pass
	g.cleanup()					#clean-up resources
