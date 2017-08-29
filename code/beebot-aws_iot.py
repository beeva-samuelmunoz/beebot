# -*- coding: utf-8 -*-


from body.body import Body
from controllers.aws_iot import AWS_IOT as controllers


PATH_CERTS = '~/beebot/data/AWS_certs/'


controller = AWS_IOT(
    body=Body(),
    client_id="awsrobot",
    endpoint_host="ayfx1339oonle.iot.us-east-1.amazonaws.com",
    endpoint_port=8883,
    path_ca=PATH_CERTS+"VeriSign-Class 3-Public-Primary-Certification-Authority-G5.pem",
    path_key=PATH_CERTS+"bcf529f7b5-private.pem.key",
    path_cert=PATH_CERTS+"bcf529f7b5-certificate.pem.crt"
)
