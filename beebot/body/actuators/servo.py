# -*- coding: utf-8 -*-


import time

import RPi.GPIO as GPIO


class Servo:

	def __init__(self, pin, deg_min, deg_max, dc_min, dc_max, pwm_freq):
		self.pin, self.deg_min, self.deg_max, self.dc_min, self.dc_max, self.pwm_freq = pin, deg_min, deg_max, dc_min, dc_max, pwm_freq
		self.status = 0  # Degrees
		# Initialize HW
		GPIO.setup(self.pin, GPIO.OUT)
		self.servo = GPIO.PWM(self.pin, self.pwm_freq)
		self.servo.start(0)


	def deg2dc(self, degrees):
		return (degrees-self.deg_min)/(self.deg_max-self.deg_min)*(self.dc_max-self.dc_min)+self.dc_min


	def stop(self):
		"""Release resources
		"""
		self.servo.stop()


	def set(self, degrees, sg=0.5):
		"""Move the servo to degrees in sg time.
		"""
		if self.deg_min <= degrees <= self.deg_max:
			self.servo.ChangeDutyCycle(self.deg2dc(degrees))
			time.sleep(sg)
			self.servo.ChangeDutyCycle(0)  # Stop servo, save energy
			# If necesary, smooth motion
			self.status = degrees


	def set_relative(self, degrees, sg=0.5):
		"""Move servo +- degrees relative to current position
		"""
		self.set(self.status+degrees, sg)
