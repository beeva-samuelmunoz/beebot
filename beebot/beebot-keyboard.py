# -*- coding: utf-8 -*-


from body.body import Body
from controllers.keyboard import Keyboard


print("Press Ctrl-D to exit:")
try:
    body = Body()
    Keyboard(body).loop()
except Exception as e:
    print(e.message)
finally:
    body.stop()
print("Hasta la vista.")
