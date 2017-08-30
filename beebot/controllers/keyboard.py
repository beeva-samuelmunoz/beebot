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
                self.move_servo('shoulder_right', +10)
            elif key=='o':
                self.move_servo('shoulder_right', -10)
            elif key=='ñ':
                self.move_servo('elbow_right', +10)
            elif key=='k':
                self.move_servo('elbow_right', -10)
            # Left arm
            elif key=='h':
                self.move_servo('shoulder_left', +10)
            elif key=='y':
                self.move_servo('shoulder_left', -10)
            elif key=='j':
                self.move_servo('elbow_left', +10)
            elif key=='g':
                self.move_servo('elbow_left', -10)
            # Platform
            elif key=='arrow_up':
                self.body.resources['platform'].forward(.1)
            elif key=='arrow_down':
                self.body.resources['platform'].backward(.1)
            elif key=='arrow_right':
                self.body.resources['platform'].turn_right(.1)
            elif key=='arrow_left':
                self.body.resources['platform'].turn_left(.1)
            # Head
            elif key=='w':
                self.move_servo('head_tilt', -10)
            elif key=='s':
                self.move_servo('head_tilt', +10)
            elif key=='d':
                self.move_servo('head_pan', -10)
            elif key=='a':
                self.move_servo('head_pan', +10)
            # Webcam
            elif key=='c':
                webcam = self.body.resources['webcam']
                if webcam.is_playing:
                    webcam.stop()
                else:
                    webcam.start()


    def move_servo(self, servo_name, deg):
        """Increase the servo position by deg degrees
        """
        servo = self.body.resources[servo_name]
        servo.move(servo.status+deg, 0.1)


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
