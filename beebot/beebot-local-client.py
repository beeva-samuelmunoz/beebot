# -*- coding: utf-8 -*-


from clients.local import Local
from body.body import Body
from controllers.keyboard import Keyboard


try:
    body = Body()
    print("Press Ctrl-D to exit:")
    client = Local(body)
    Keyboard(client).loop()
except Exception as e:
    print(e.message)
finally:
    body.stop()
print("Hasta la vista.")
