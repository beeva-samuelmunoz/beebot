# -*- coding: utf-8 -*-


import RPi.GPIO as GPIO

from .actuators.laser import Laser
from .actuators.platform import Platform
from .actuators.servo import Servo
from .sensors.button import Button
from .sensors.dht11 import DHT11
from .sensors.webcam_streamer import WebcamStreamer


class Body:

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        # Body configuration
        self.resources = {}
        """
        SHOULDERS
            HW: Tower Pro MG90S
            Min: 0º arm is up
            Max: 180º arm is down
        """
        self.resources['shoulder_right'] = Servo(
            pin=4,
            deg_min=0,
            deg_max=180,
            dc_min=2,
            dc_max=12,
            pwm_freq=50
        )
        self.resources['shoulder_left'] = Servo(
            pin=16,
            deg_min=0,
            deg_max=180,
            dc_min=2.5,
            dc_max=12.5,
            pwm_freq=50
        )
        # Unify movement, move servos to certain degrees
        self.resources['shoulder_right'].move = self.resources['shoulder_right'].set
        self.resources['shoulder_left'].move = lambda deg: self.resources['shoulder_left'].set((180-deg)%181)
        # Initial status
        self.resources['shoulder_right'].move(180)
        self.resources['shoulder_left'].move(180)

        """
        ELBOWS
            HW: Tower Pro SG90
            Min: 70º elbow is flexed
            Max: 180º elbow is extended
        """
        self.resources['elbow_right'] = Servo(
            pin=11,
            deg_min=70,
            deg_max=180,
            dc_min=6.8,
            dc_max=13,
            pwm_freq=50
        )
        self.resources['elbow_left'] = Servo(
            pin=23,
            deg_min=0,
            deg_max=110,
            dc_min=3,
            dc_max=9.111,
            pwm_freq=50
        )
        # Unify movement, move servos to certain degrees
        self.resources['elbow_right'].move = self.resources['elbow_right'].set
        self.resources['elbow_left'].move = lambda deg: self.resources['elbow_left'].set((180-deg)%181)
        self.resources['elbow_right'].move(180)
        self.resources['elbow_left'].move(180)

        """
        HEAD (pan and tilt)
            HW: Tower Pro SG90
            Min: 0º elbow is flexed
            Max: 180º elbow is extended
        """
        self.resources['head_pan'] = Servo(
            pin=2,
            deg_min=0,
            deg_max=180,
            dc_min=3,
            dc_max=13,
            pwm_freq=50
        )
        self.resources['head_tilt'] = Servo(
            pin=14,
            deg_min=0,
            deg_max=180,
            dc_min=3,
            dc_max=13,
            pwm_freq=50
        )
        self.resources['head_pan'].move = self.resources['head_pan'].set
        self.resources['head_tilt'].move = self.resources['head_tilt'].set
        self.resources['head_pan'].move(90)
        self.resources['head_tilt'].move(90)

        """
        PLATFORM
        """
        self.resources['platform']  = Platform(
            in1=6,
            in2=13,
            in3=19,
            in4=26,
        )
        self.resources['platform'].stop()

        """
        WEBCAM
        """
        self.resources['webcam'] = WebcamStreamer('cvlc --no-audio v4l2:///dev/video0:width=800:height=600 --v4l2-fps 30 --sout "#transcode{vcodec=MJPG,vb=1600,fps=10}:standard{access=http,mux=mpjpeg,dst=:18223/}" --sout-http-mime="multipart/x-mixed-replace;boundary=--7b3cc56e5f51db803f790dad720ed50a"')

        """
        TEMPERATURE/HUMIDITY SENSOR
            DHT11
        """
        self.resources['dht11'] = DHT11(
            pin=7
        )
        self.resources['dht11'].stop = lambda : None  # Dummy function

        """
        LASER
            Diode
        """
        self.resources['laser'] = Laser(
            pin=22
        )
        self.resources['laser'].stop = lambda : None  # Dummy function

        """
        BUTTON
        """
        self.resources['button'] = Button(
            pin=24
        )


    def stop(self):
        """Stop body and release resources
        """
        for resource in self.resources.values():
            resource.stop()
        GPIO.cleanup()
