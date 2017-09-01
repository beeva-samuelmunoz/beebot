# -*- coding: utf-8 -*-


import time

""" See:
- https://pypi.python.org/pypi/AWSIoTPythonSDK
- https://s3.amazonaws.com/aws-iot-device-sdk-python-docs/sphinx/html/generated/AWSIoTPythonSDK.MQTTLib.html#AWSIoTPythonSDK.MQTTLib.AWSIoTMQTTClient
"""
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient


class AWS_IOT:

    def __init__(self,
        client_id,
        endpoint_host, endpoint_port ,  # Endpoint
        path_ca, path_key, path_cert,   # Credentials
    ):
        # AWS IoT Client
        self.client = AWSIoTMQTTClient(client_id)
        self.client.configureEndpoint(endpoint_host, endpoint_port)
        self.client.configureCredentials(path_ca, path_key, path_cert)
        self.client.configureOfflinePublishQueueing(queueSize=-1)  # Infinite
        self.client.configureDrainingFrequency(frequencyInHz=2)
        self.client.configureConnectDisconnectTimeout(timeoutSecond=10)
        self.client.configureMQTTOperationTimeout(timeoutSecond=5)
        self.client.configureAutoReconnectBackoffTime(
            baseReconnectQuietTimeSecond=1,
            maxReconnectQuietTimeSecond=25,
            stableConnectionTimeSecond=40
        )


    def event(self, ev):
        # Right arm
        if ev=='shoulder_right_down':
        elif ev=='shoulder_right_up':
        elif ev=='elbow_right_down':
        elif ev=='elbow_right_up':
        # Left arm
        elif ev=='shoulder_left_down':
        elif ev=='shoulder_left_up':
        elif ev=='elbow_left_down':
        elif ev=='elbow_left_up':
        # Platform
        elif ev=='platform_forward':
        elif ev=='platform_backward':
        elif ev=='platform_right':
        elif ev=='platform_left':
        # Head
        elif ev=='head_tilt_up':
        elif ev=='head_tilt_down':
        elif ev=='head_pan_right':
        elif ev=='head_pan_left':
        # Webcam
        elif ev=='c':
            webcam = self.body.resources['webcam']
            if webcam.is_playing:
                webcam.stop()
            else:
                webcam.start()


        # # Topic: Action
        # self.TOPIC2ACTION = {  # MQTT actuator topics
        #     # Arms
        #     "beebot/shoulder_right": self.body.resources['shoulder_right'].move,
        #     "beebot/shoulder_left": self.body.resources['shoulder_left'].move,
        #     "beebot/elbow_right": self.body.resources['elbow_right'].move,
        #     "beebot/elbow_left": self.body.resources['elbow_left'].move,
        #     # Platform
        #     "beebot/platform/forward": self.body.resources['platform'].forward,
        #     "beebot/platform/backward": self.body.resources['platform'].backward,
        #     "beebot/platform/turn_left": self.body.resources['platform'].turn_left,
        #     "beebot/platform/turn_right": self.body.resources['platform'].turn_right,
        #     "beebot/platform/stop": self.body.resources['platform'].stop,
        #     # Head
        #     "beebot/head_pan": self.body.resources['head_pan'].move,
        #     "beebot/head_tilt": self.body.resources['head_tilt'].move,
        #     # Webcam
        #     "beebot/webcam/start": self.body.resources['webcam'].start,
        #     "beebot/webcam/stop": self.body.resources['webcam'].stop,
        # }
        # # Actuators: subscribe to topics
        # for topic in self.TOPIC2ACTION.keys():
        #     self.client.subscribe(topic, 1, self._msg_parser)


    # def _msg_parser(self, client_id, user_data, msg):
    #     action = msg.topic('/')[-1]
    #     status = None
    #     if action in {'start','stop'}:  #No payload actions
    #         self.TOPIC2ACTION[msg.topic]()
    #         status = 0 if action=='stop' else 1
    #     else:
    #         try:
    #             payload = float(msg.payload)
    #             self.TOPIC2ACTION[msg.topic](payload)
    #             status = payload
    #         except Exception as e:
    #             print(e.message)
    #     if status:
    #         self.client.publish(msg.topic+"/status", str(status) , 0)
