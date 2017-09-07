# -*- coding: utf-8 -*-


import time

import RPi.GPIO as GPIO


class Laser:

	def __init__(self, pin):
		self.pin = pin
		GPIO.setup(self.pin, GPIO.OUT)


	def fire(self):
		for i in range(10):
			GPIO.output(self.pin, GPIO.HIGH)
			time.sleep(0.1)
			GPIO.output(self.pin, GPIO.LOW)
			time.sleep(0.2)
