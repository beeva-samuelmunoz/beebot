# -*- coding: utf-8 -*-


import RPi.GPIO as GPIO


class Button:

    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)


    def set_callback(self, callback):
        GPIO.add_event_detect(self.pin, GPIO.RISING, callback=self.callback)


    def stop(self):
        GPIO.remove_event_detect(self.pin)
