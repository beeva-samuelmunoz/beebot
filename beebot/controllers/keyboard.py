# -*- coding: utf-8 -*-


import time
import os
import sys


class Keyboard:

    def __init__(self, body):
        self.body = body


    def loop(self):
        key = 0
        exit = False
        resources = self.body.resources
        while not exit:
            key = self._wait_key()
            # Arrows
            if ord(key) == 4:
                key = 'CTRL+D'
            elif ord(key)==27:  # Arrow keys
                key = self._wait_key()
                if ord(key)==91:
                    k = ord(self._wait_key())
                    key = {
                    66: 'arrow_down',
                    65: 'arrow_up',
                    67: 'arrow_right',
                    68: 'arrow_left'
                    }.get(k)
            # Act upon key
            print(key)
            if key=='CTRL+D':
                exit = True
            # Right arm
            elif key=='l':
                resources['shoulder_right'].set_relative(+10, 0.1)
            elif key=='o':
                resources['shoulder_right'].set_relative(-10, 0.1)
            elif key=='ñ':
                resources['elbow_right'].set_relative(+10, 0.1)
            elif key=='k':
                resources['elbow_right'].set_relative(-10, 0.1)
            # Left arm
            elif key=='L':
                resources['shoulder_left'].set_relative(-10, 0.1)
            elif key=='O':
                resources['shoulder_left'].set_relative(+10, 0.1)
            elif key=='Ñ':
                resources['shoulder_left'].set_relative(-10, 0.1)
            elif key=='K':
                resources['shoulder_left'].set_relative(+10, 0.1)
            # Platform
            elif key=='arrow_up':
                resources['platform'].forward(0.1)
            elif key=='arrow_down':
                resources['platform'].backward(0.1)
            elif key=='arrow_right':
                resources['platform'].turn_right(0.1)
            elif key=='arrow_left':
                resources['platform'].turn_left(0.1)
            # Head
            elif key=='w':
                resources['head_tilt'].set_relative(-10, 0.1)
            elif key=='s':
                resources['head_tilt'].set_relative(+10, 0.1)
            elif key=='d':
                resources['head_pan'].set_relative(-10, 0.1)
            elif key=='a':
                resources['head_pan'].set_relative(+10, 0.1)
            # Webcam
            elif key=='c':
                webcam = self.body.resources['webcam']
                if webcam.is_playing:
                    webcam.stop()
                else:
                    webcam.start()


    @staticmethod
    def _wait_key():
        """ Wait for a key press on the console and return it.
        From: https://stackoverflow.com/questions/983354/how-do-i-make-python-to-wait-for-a-pressed-key
        """
        result = None
        if os.name == 'nt':
            import msvcrt
            result = msvcrt.getch()
        else:
            import termios
            fd = sys.stdin.fileno()
            oldterm = termios.tcgetattr(fd)
            newattr = termios.tcgetattr(fd)
            newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
            termios.tcsetattr(fd, termios.TCSANOW, newattr)
            try:
                result = sys.stdin.read(1)
            except IOError:
                pass
            finally:
                termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
        return result
