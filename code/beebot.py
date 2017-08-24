
import time

from body.body import Body



b = Body()
time.sleep(5)

b.resources['elbow_right'].move(90)
b.resources['elbow_left'].move(90)
time.sleep(2)
b.resources['shoulder_right'].move(0)
b.resources['shoulder_left'].move(0)
time.sleep(2)
b.resources['elbow_right'].move(180)
b.resources['elbow_left'].move(180)


# b.resources['platform'].forward(0.3)
