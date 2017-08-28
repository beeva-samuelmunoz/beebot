
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
        # Topic: Action
        self.TOPIC2ACTION = {  # MQTT actuator topics
            # Arms
            "beebot/shoulder_right": self.body['shoulder_right'].move,
            "beebot/shoulder_left": self.body['shoulder_left'].move,
            "beebot/elbow_right": self.body['elbow_right'].move,
            "beebot/elbow_left": self.body['elbow_left'].move,
            # Platform
            "beebot/platform/forward": self.body['platform'].forward,
            "beebot/platform/backward": self.body['platform'].backward,
            "beebot/platform/turn_left": self.body['platform'].turn_left,
            "beebot/platform/turn_right": self.body['platform'].turn_right,
            "beebot/platform/stop": self.body['platform'].stop,
            # Head
            "beebot/head_pan": self.body['head_pan'].move,
            "beebot/head_tilt": self.body['head_tilt'].move,
        }
        # Actuators: subscribe to topics
        for topic in self.TOPIC2ACTION.keys():
            self.client.subscribe(topic, 1, self._msg_parser)


    def _msg_parser(self, client_id, user_data, msg):
        try:
            payload = float(payload)
            self.TOPIC2ACTION[msg.topic](payload)
            self.client.publish(msg.topic+"/status", str(payload), 0)
        except Exception as e:
            print(e.message)
