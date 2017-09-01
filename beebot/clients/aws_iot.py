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
        self.client.configureEndpoint(
            hostName=endpoint_host,
            portNumber=endpoint_port
        )
        self.client.configureCredentials(
            CAFilePath=path_ca,
            KeyPath=path_key,
            CertificatePath=path_cert
        )
        self.client.configureOfflinePublishQueueing(queueSize=-1)  # Infinite
        self.client.configureDrainingFrequency(frequencyInHz=2)
        self.client.configureConnectDisconnectTimeout(timeoutSecond=10)
        self.client.configureMQTTOperationTimeout(timeoutSecond=5)
        self.client.configureAutoReconnectBackoffTime(
            baseReconnectQuietTimeSecond=1,
            maxReconnectQuietTimeSecond=25,
            stableConnectionTimeSecond=40
        )
        self.client.connect(keepAliveIntervalSecond=60)


    def stop(self):
        self.client.disconnect()


    def event(self, ev):
        print(ev)
        # Right arm
        if ev=='shoulder_right_down':
            self.client.publish("beebot/shoulder_right", 10 , 0)
        elif ev=='shoulder_right_up':
            self.client.publish("beebot/shoulder_right", -10 , 0)
        elif ev=='elbow_right_down':
            self.client.publish("beebot/elbow_right", -10 , 0)
        elif ev=='elbow_right_up':
            self.client.publish("beebot/elbow_right", -10 , 0)
        # # Left arm
        elif ev=='shoulder_left_down':
            self.client.publish("beebot/shoulder_left", -10 , 0)
        elif ev=='shoulder_left_up':
            self.client.publish("beebot/shoulder_left", 10 , 0)
        elif ev=='elbow_left_down':
            self.client.publish("beebot/elbow_left", -10 , 0)
        elif ev=='elbow_left_up':
            self.client.publish("beebot/elbow_left", +10 , 0)
        # # Platform
        elif ev=='platform_forward':
        elif ev=='platform_backward':
        elif ev=='platform_right':
        elif ev=='platform_left':
        # # Head
        # elif ev=='head_tilt_up':
        # elif ev=='head_tilt_down':
        # elif ev=='head_pan_right':
        # elif ev=='head_pan_left':
        # # Webcam
        # elif ev=='camera_switch':
        #     webcam = self.body.resources['webcam']
        #     if webcam.is_playing:
        #         webcam.stop()
        #     else:
        #         webcam.start()





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
