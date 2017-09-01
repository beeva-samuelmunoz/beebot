# -*- coding: utf-8 -*-


from body.body import Body
from backends.aws_iot import AWS_IOT
from config_local import PATH_DATA


PATH_CERTS = PATH_DATA+'AWS_iot-beebot/'

backend = AWS_IOT(
    body=Body(),
    client_id="awsrobot",
    endpoint_host="ayfx1339oonle.iot.us-east-1.amazonaws.com",
    endpoint_port=8883,
    path_ca=PATH_CERTS+"VeriSign-Class 3-Public-Primary-Certification-Authority-G5.pem",
    path_key=PATH_CERTS+"bcf529f7b5-private.pem.key",
    path_cert=PATH_CERTS+"bcf529f7b5-certificate.pem.crt"
)
