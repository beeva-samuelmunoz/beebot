# -*- coding: utf-8 -*-


import time
import os
import sys


class Local:

    def __init__(self, body):
        self.body = body


    def event(self, ev):
        # Right arm
        if ev=='shoulder_right_down':
            self.body.resources['shoulder_right'].set_relative(+10, 0.1)
        elif ev=='shoulder_right_up':
            self.body.resources['shoulder_right'].set_relative(-10, 0.1)
        elif ev=='elbow_right_down':
            self.body.resources['elbow_right'].set_relative(+10, 0.1)
        elif ev=='elbow_right_up':
            self.body.resources['elbow_right'].set_relative(-10, 0.1)
        # Left arm
        elif ev=='shoulder_left_down':
            self.body.resources['shoulder_left'].set_relative(-10, 0.1)
        elif ev=='shoulder_left_up':
            self.body.resources['shoulder_left'].set_relative(+10, 0.1)
        elif ev=='elbow_left_down':
            self.body.resources['shoulder_left'].set_relative(-10, 0.1)
        elif ev=='elbow_left_up':
            self.body.resources['shoulder_left'].set_relative(+10, 0.1)
        # Platform
        elif ev=='platform_forward':
            self.body.resources['platform'].forward(0.1)
        elif ev=='platform_backward':
            self.body.resources['platform'].backward(0.1)
        elif ev=='platform_right':
            self.body.resources['platform'].turn_right(0.1)
        elif ev=='platform_left':
            self.body.resources['platform'].turn_left(0.1)
        # Head
        elif ev=='head_tilt_up':
            self.body.resources['head_tilt'].set_relative(-10, 0.1)
        elif ev=='head_tilt_down':
            self.body.resources['head_tilt'].set_relative(+10, 0.1)
        elif ev=='head_pan_right':
            self.body.resources['head_pan'].set_relative(-10, 0.1)
        elif ev=='head_pan_left':
            self.body.resources['head_pan'].set_relative(+10, 0.1)
        # Webcam
        elif ev=='c':
            webcam = self.body.resources['webcam']
            if webcam.is_playing:
                webcam.stop()
            else:
                webcam.start()
