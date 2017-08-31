# -*- coding: utf-8 -*-


import time
import os
import sys


class Local:

    def __init__(self, body):
        self.body = body

    def event(self, ev):
        # Right arm
        elif ev=='l':
            self.body.resources['shoulder_right'].set_relative(+10, 0.1)
        elif ev=='o':
            self.body.resources['shoulder_right'].set_relative(-10, 0.1)
        elif ev=='ñ':
            self.body.resources['elbow_right'].set_relative(+10, 0.1)
        elif ev=='k':
            self.body.resources['elbow_right'].set_relative(-10, 0.1)
        # Left arm
        elif ev=='L':
            self.body.resources['shoulder_left'].set_relative(-10, 0.1)
        elif ev=='O':
            self.body.resources['shoulder_left'].set_relative(+10, 0.1)
        elif ev=='Ñ':
            self.body.resources['shoulder_left'].set_relative(-10, 0.1)
        elif ev=='K':
            self.body.resources['shoulder_left'].set_relative(+10, 0.1)
        # Platform
        elif ev=='arrow_up':
            self.body.resources['platform'].forward(0.1)
        elif ev=='arrow_down':
            self.body.resources['platform'].backward(0.1)
        elif ev=='arrow_right':
            self.body.resources['platform'].turn_right(0.1)
        elif ev=='arrow_left':
            self.body.resources['platform'].turn_left(0.1)
        # Head
        elif ev=='w':
            self.body.resources['head_tilt'].set_relative(-10, 0.1)
        elif ev=='s':
            self.body.resources['head_tilt'].set_relative(+10, 0.1)
        elif ev=='d':
            self.body.resources['head_pan'].set_relative(-10, 0.1)
        elif ev=='a':
            self.body.resources['head_pan'].set_relative(+10, 0.1)
        # Webcam
        elif ev=='c':
            webcam = self.body.resources['webcam']
            if webcam.is_playing:
                webcam.stop()
            else:
                webcam.start()
