# -*- coding: utf-8 -*-


from body.body import Body
from controllers.keyboard import Keyboard


try:
    body = Body()
    print("Press Ctrl-D to exit:")
    Keyboard(body).loop()
except Exception as e:
    print(e.message)
finally:
    body.stop()
print("Hasta la vista.")
