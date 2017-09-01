# -*- coding: utf-8 -*-

from clients.aws_iot import AWS_IOT
from controllers.keyboard import Keyboard
from config_local import PATH_DATA


PATH_CERTS = PATH_DATA+'AWS_iot-client/'

try:
    print("Press Ctrl-D to exit:")
    client = AWS_IOT(
        client_id="awsrobot",
        endpoint_host="ayfx1339oonle.iot.us-east-1.amazonaws.com",
        endpoint_port=8883,
        path_ca=PATH_CERTS+"VeriSign-Class 3-Public-Primary-Certification-Authority-G5.pem",
        path_key=PATH_CERTS+"fb79c34b36-private.pem.key",
        path_cert=PATH_CERTS+"fb79c34b36-certificate.pem.crt"
    )
    Keyboard(client).loop()
except Exception as e:
    print(e.message)
finally:
    client.stop()
print("Hasta la vista.")
