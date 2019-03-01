#
#  Piper.py
#  Rubik's Cube Solver
#
#  Created by Blake Williams on 1/10/19.
#  Copyright © 2019 Blake Williams. All rights reserved.
#


import RPi.GPIO as G
from time import sleep

def MotMov(direction,dirPin,stepPin):
	G.output(dirPin,direction)
	delay = .005
	for i in range(100):
		delay = 1/((15 * i) + 200)
		G.output(stepPin,1)
		sleep(delay)
		G.output(stepPin,0)
		sleep(delay)
	for i in range(100):
		delay = 1/((-15 * (i+100)) + 3800)
		G.output(stepPin,1)
		sleep(delay)
		G.output(stepPin,0)
		sleep(delay)

def Log(moves):
	G.setmode(GPBOARD)
	G.setup(12,G.OUT) # UC
	G.setup(16,G.OUT) # UCC
	G.setup(18,G.OUT) # DC
	G.setup(22,G.OUT) # DCC
	G.setup(32,G.OUT) # LC
	G.setup(36,G.OUT) # LCC
	G.setup(38,G.OUT) # RC
	G.setup(40,G.OUT) # RCC
	G.setup(37,G.OUT) # FC
	G.setup(35,G.OUT) # FCC
	G.setup(33,G.OUT) # BC
	G.setup(31,G.OUT) # BCC
	print(moves)


	try:
		for code in moves:
			if code == 'UC':
				MotMov()
			elif code == 'UCC':
				MotMov()
			elif code == 'DC':
				MotMov()
			elif code == 'DCC':
				MotMov()
			elif code == 'LC':
				MotMov()
			elif code == 'LCC':
				MotMov()
			elif code == 'RC':
				MotMov()
			elif code == 'RCC':
				MotMov()
			elif code == 'FC':
				MotMov()
			elif code == 'FCC':
				MotMov()
			elif code == 'BC':
				MotMov()
			elif code == 'BCC':
				MotMov()
	except KeyboardInterrupt:
		GPIO.cleanup()

	GPIO.cleanup()