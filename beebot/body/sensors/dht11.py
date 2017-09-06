# -*- coding: utf-8 -*-
"""
HW: DHT11 temperature/humidity sensor
SPECS: http://www.micropik.com/PDF/dht11.pdf

Adapted from: http://www.uugear.com/portfolio/dht11-humidity-temperature-sensor-module/
"""

import time

import RPi.GPIO as GPIO


class DHT11:

	def __init__(self, pin):
		self.pin = pin
		GPIO.setup(self.pin, GPIO.OUT)


	def read(self):
		GPIO.output(self.pin, GPIO.HIGH)
		time.sleep(0.025)
		GPIO.output(self.pin, GPIO.LOW)
		time.sleep(0.02)
		GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		data = [ GPIO.input(self.pin) for _ in range(0, 500)]

		bit_count = 0
		tmp = 0
		count = 0
		humidity_bit = ""
		temperature_bit = ""
		crc = ""
		try:
			while data[count] == 1:
				tmp = 1
				count += 1
			for i in range(0, 32):
				bit_count = 0
				while data[count] == 0:
					tmp = 1
					count += 1
				while data[count] == 1:
					bit_count += 1
					count += 1
				if bit_count > 3:
					if i>=0 and i<8:
						humidity_bit = humidity_bit+"1"
					if i>=16 and i<24:
						temperature_bit = temperature_bit + "1"
				else:
					if i>=0 and i<8:
						humidity_bit = humidity_bit + "0"
					if i>=16 and i<24:
						temperature_bit = temperature_bit + "0"
		except:
			raise Exception("ERR_RANGE")

		try:
			for i in range(0, 8):
				bit_count = 0
				while data[count] == 0:
					tmp = 1
					count += 1
				while data[count] == 1:
					bit_count += 1
					count += 1
				if bit_count > 3:
					crc = crc + "1"
				else:
					crc = crc + "0"
		except:
			raise Exception("ERR_RANGE")

		humidity = self._bin2dec(humidity_bit)
		temperature = self._bin2dec(temperature_bit)
		if int(humidity) + int(temperature) - int(self._bin2dec(crc)) != 0:
			raise Exception("ERR_CRC")
		return (temperature, humidity)


	def _bin2dec(self, string_num):
		return str(int(string_num, 2))
