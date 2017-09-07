# -*- coding: utf-8 -*-


import threading
import time


class Local:

    def __init__(self, body):
        self.body = body
        self.stop = False
        self.worker_dht11 = threading.Thread(
                name="worker_dht11",
                target=self._print_dht11
        )
        worker_dht11.start()


    def _print_dht11(self):
        temp, hum = 0, 0
        while not self.stop:
            while hum==0:
                time.sleep(0.5)
                dht11 = self.body.resources['dht11'].read()
                temp, hum = dht11.temperature, dht11.humidity
            print("DHT11 - Temperature: {}".format(temp))
            print("DHT11 - Humidity: {}".format(hum))


    def stop(self):
        self.stop = True
        worker_dht11.join()


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
            self.body.resources['elbow_left'].set_relative(-10, 0.1)
        elif ev=='elbow_left_up':
            self.body.resources['elbow_left'].set_relative(+10, 0.1)
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
        elif ev=='camera_switch':
            self.body.resources['webcam'].switch()
        # Laser
        elif ev=='laser':
            self.body.resources['laser'].fire()
