# -*- coding: utf-8 -*-


import time
import os
import sys


class Keyboard:

    def __init__(self, client):
        self.client = client
        self.key2event = {  # Key mapping
            # Right arm
            'o': 'shoulder_right_up',
            'l': 'shoulder_right_down',
            'k': 'elbow_right_up',
            'ñ': 'elbow_right_down',
            # Left arm
            'O': 'shoulder_left_up',
            'L': 'shoulder_left_down',
            'K': 'elbow_left_up',
            'Ñ': 'elbow_left_down',
            # Platform
            'arrow_up': 'platform_forward',
            'arrow_down': 'platform_backward',
            'arrow_right': 'platform_right',
            'arrow_left': 'platform_left',
            # Head
            'w': 'head_tilt_up',
            's': 'head_tilt_down',
            'a': 'head_pan_left',
            'd': 'head_pan_right',
            # Camera
            'c': 'camera_switch',
            ' ': 'laser'
        }


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
            if key=='CTRL+D':
                exit = True
            else:
                event = self.key2event.get(key, None)
                if event:
                    self.client.event(event)


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
