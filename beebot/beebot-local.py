# -*- coding: utf-8 -*-


from backends.local import Local
from body.body import Body
from controllers.keyboard import Keyboard


try:
    body = Body()
    print("Press Ctrl-D to exit:")
    backend = Local(body)
    Keyboard(backend).loop()
except Exception as e:
    print(e.message)
finally:
    body.stop()
print("Hasta la vista.")
