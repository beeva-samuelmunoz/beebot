# -*- coding: utf-8 -*-


import time

from body.body import Body



b = Body()
time.sleep(5)

b.resources['elbow_right'].move(90)
b.resources['elbow_left'].move(90)
time.sleep(1)
b.resources['shoulder_right'].move(0)
b.resources['shoulder_left'].move(0)
time.sleep(.5)
b.resources['elbow_right'].move(180)
b.resources['elbow_left'].move(180)
time.sleep(3)
b.resources['head_pan'].move(50)
time.sleep(.5)
b.resources['head_pan'].move(130)
time.sleep(.5)
b.resources['head_pan'].move(90)
time.sleep(.5)
b.resources['head_tilt'].move(130)
time.sleep(.5)
b.resources['head_tilt'].move(50)
time.sleep(.5)
b.resources['head_tilt'].move(90)

b.stop()

b = Body()
b.stop()

# b.resources['platform'].forward(0.3)
