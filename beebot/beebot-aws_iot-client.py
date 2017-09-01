# -*- coding: utf-8 -*-

from clients.aws_iot import AWS_IOT
from body.body import Body
from controllers.keyboard import Keyboard


PATH_CERTS = '~/beebot/data/AWS_iot-client/'
try:
    body = Body()
    print("Press Ctrl-D to exit:")
    client = AWS_IOT(
        body=body,
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
    body.stop()
print("Hasta la vista.")
