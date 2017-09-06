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

        # Topic: Action
        self.TOPIC2ACTION = {  # MQTT actuator topics
            # Arms
            "beebot/dht11/temperature": print,
            "beebot/dht11/humidity": print,
        }
        # Actuators: subscribe to topics
        for topic in self.TOPIC2ACTION.keys():
            self.client.subscribe(topic, 1, self._msg_parser)


    def _msg_parser(self, client_id, user_data, msg):
        try:
            payload = float(msg.payload)
            self.TOPIC2ACTION[msg.topic]("<-\tTopic:{}\tMessage:{}".format(msg.topic, payload))
            status = payload
        except Exception as e:
            print(e)


    def stop(self):
        self.client.disconnect()


    def event(self, ev):
        print("->\tEvent: {}".format(ev))
        # Right arm
        if ev=='shoulder_right_down':
            self.client.publish("beebot/shoulder_right", +10, 0)
        elif ev=='shoulder_right_up':
            self.client.publish("beebot/shoulder_right", -10, 0)
        elif ev=='elbow_right_down':
            self.client.publish("beebot/elbow_right", +10, 0)
        elif ev=='elbow_right_up':
            self.client.publish("beebot/elbow_right", -10, 0)
        # Left arm
        elif ev=='shoulder_left_down':
            self.client.publish("beebot/shoulder_left", -10, 0)
        elif ev=='shoulder_left_up':
            self.client.publish("beebot/shoulder_left", +10, 0)
        elif ev=='elbow_left_down':
            self.client.publish("beebot/elbow_left", -10, 0)
        elif ev=='elbow_left_up':
            self.client.publish("beebot/elbow_left", +10, 0)
        # Platform
        elif ev=='platform_forward':
            self.client.publish("beebot/platform/forward", 0.1, 0)
        elif ev=='platform_backward':
            self.client.publish("beebot/platform/backward", 0.1, 0)
        elif ev=='platform_right':
            self.client.publish("beebot/platform/turn_right", 0.1, 0)
        elif ev=='platform_left':
            self.client.publish("beebot/platform/turn_left", 0.1, 0)
        # Head
        elif ev=='head_tilt_up':
            self.client.publish("beebot/head_tilt", -10, 0)
        elif ev=='head_tilt_down':
            self.client.publish("beebot/head_tilt", +10, 0)
        elif ev=='head_pan_right':
            self.client.publish("beebot/head_pan", -10, 0)
        elif ev=='head_pan_left':
            self.client.publish("beebot/head_pan", +10, 0)
        # Webcam
        elif ev=='camera_switch':
            self.client.publish("beebot/webcam/switch", 0, 0)
        # Laser
        elif ev=='laser':
            self.client.publish("beebot/laser/fire", 0, 0)
