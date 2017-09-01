# -*- coding: utf-8 -*-


import shlex
import subprocess
import threading
import time



class CommandPlayer(threading.Thread):

    def __init__(self, command, callback= lambda: None):
        """Constructor

        Parameters
        ----------
        command : str
            Command to execute.
        callback: function
            Function to call after the command is successfully executed.
        """
        self.command = command
        self.callback = callback
        self.process = None
        super(self.__class__, self).__init__()


    def run(self):
        """Thread method override.
        """
        self.process = subprocess.Popen(shlex.split(self.command))
        self.process.wait()
        if self.process.returncode == 0:  # Process was not killed
            self.callback()

    def stop(self):
        """Stop the command execution.
        """
        self.process.kill()



class WebcamStreamer(object):

    def __init__(self, player_command):
        self.player_command = player_command
        self.is_playing = False
        self.tstamp_play = None  # When command was launched

    def start(self, position=None):
        """Start streaming.
        """
        if not self.is_playing:
            self.tstamp_play = time.time()
            self.is_playing = True
            self.thread = CommandPlayer(self.player_command)
            self.thread.start()

    def stop(self):
        """If an element is being played, stop.
        """
        if self.is_playing:
            self.is_playing = False
            self.tstamp_play = None
            self.thread.stop()

    def switch(self):
        """Change state start/stop
        """
        if self.is_playing:
            self.stop()
        else:
            self.start()
