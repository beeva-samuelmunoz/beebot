# -*- coding: utf-8 -*-


import time

import RPi.GPIO as GPIO


class Platform:

	def __init__(self, in1, in2, in3, in4):
		self.inputs = [in1, in2, in3, in4]

		# Initialize HW
		for input in self.inputs:
			GPIO.setup(input, GPIO.OUT)


	def forward(self, sg):
		self.action([GPIO.LOW, GPIO.HIGH, GPIO.LOW, GPIO.HIGH])
		time.sleep(sg)
		self.stop()


	def backward(self, sg):
		self.action([GPIO.HIGH, GPIO.LOW, GPIO.HIGH, GPIO.LOW])
		time.sleep(sg)
		self.stop()


	def turn_left(self, sg):
		self.action([GPIO.LOW, GPIO.HIGH, GPIO.HIGH, GPIO.LOW])
		time.sleep(sg)
		self.stop()


	def turn_right(self, sg):
		self.action([GPIO.HIGH, GPIO.LOW, GPIO.LOW, GPIO.HIGH])
		time.sleep(sg)
		self.stop()


	def stop(self):
		self.action([GPIO.LOW, GPIO.LOW, GPIO.LOW, GPIO.LOW])


	def action(self, values):
		for input,value in zip(self.inputs, values):
			GPIO.output(input, value)
