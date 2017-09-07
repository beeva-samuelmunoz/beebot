# -*- coding: utf-8 -*-


from clients.local import Local
from body.body import Body
from controllers.keyboard import Keyboard


try:
    print("Initializing Beebot's body.")
    body = Body()
    print("I am alive!\nPress Ctrl-D to exit:")
    client = Local(body)
    Keyboard(client, 0).loop()
except Exception as e:
    print(e)
    client.stop()
finally:
    body.stop()
print("Hasta la vista.")
