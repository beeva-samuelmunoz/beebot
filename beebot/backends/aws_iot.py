# -*- coding: utf-8 -*-


import threading
import time

""" See:
- https://pypi.python.org/pypi/AWSIoTPythonSDK
- https://s3.amazonaws.com/aws-iot-device-sdk-python-docs/sphinx/html/generated/AWSIoTPythonSDK.MQTTLib.html#AWSIoTPythonSDK.MQTTLib.AWSIoTMQTTClient
"""
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient


class AWS_IOT:

    def __init__(self,
        body, client_id,
        endpoint_host, endpoint_port ,  # Endpoint
        path_ca, path_key, path_cert,   # Credentials
    ):
        self.body = body
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
        self.client.connect(keepAliveIntervalSecond=60)

        # Topic: Action
        self.TOPIC2ACTION = {  # MQTT actuator topics
            # Arms
            "beebot/shoulder_right": self.body.resources['shoulder_right'].set_relative,
            "beebot/shoulder_left": self.body.resources['shoulder_left'].set_relative,
            "beebot/elbow_right": self.body.resources['elbow_right'].set_relative,
            "beebot/elbow_left": self.body.resources['elbow_left'].set_relative,
            # Platform
            "beebot/platform/forward": self.body.resources['platform'].forward,
            "beebot/platform/backward": self.body.resources['platform'].backward,
            "beebot/platform/turn_left": self.body.resources['platform'].turn_left,
            "beebot/platform/turn_right": self.body.resources['platform'].turn_right,
            "beebot/platform/stop": self.body.resources['platform'].stop,
            # Head
            "beebot/head_pan": self.body.resources['head_pan'].set_relative,
            "beebot/head_tilt": self.body.resources['head_tilt'].set_relative,
            # Webcam
            "beebot/webcam/switch": lambda x: self.body.resources['webcam'].switch(),
            # Laser
            "beebot/laser/fire": lambda x: self.body.resources['laser'].fire(),
        }
        # Actuators: subscribe to topics
        for topic in self.TOPIC2ACTION.keys():
            self.client.subscribe(topic, 1, self._msg_parser)
        self.stop = False  # Keep running everything


    def _send_dht11(self):
        temp, hum = 0, 0
        while not self.stop:
            while hum==0:
                time.sleep(0.5)
                dht11 = self.body.resources['dht11'].read()
                temp, hum = dht11.temperature, dht11.humidity
            self.client.publish("beebot/dht11/temperature", temp , 0)
            self.client.publish("beebot/dht11/humidity", hum , 0)
            time.sleep(10)


    def loop(self):
        worker_dht11_temperature = threading.Thread(
            name="worker_dht11",
            target=self._send_dht11
        )
        worker_dht11_temperature.start()
        while not self.stop:
            time.sleep(0.05)


    def stop(self):
        self.stop = True
        worker_dht11_temperature.join()
        self.client.disconnect()


    def _msg_parser(self, client_id, user_data, msg):
        print(msg.topic)
        print(msg.payload)
        try:
            payload = float(msg.payload)
            self.TOPIC2ACTION[msg.topic](payload)
            status = payload
        except Exception as e:
            print(e)
        # TODO status move it to the loop every x segs
        # if status:
            # self.client.publish(msg.topic+"/status", str(status) , 0)
            # resource = msg.topic.split('/')
