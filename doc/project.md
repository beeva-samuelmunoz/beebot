# Project documentation

## Table of contents
* [Capabilities and Hardware]("#hardware")
* [Makefile]("#makefile")
* [Autorun]("#autorun")


## Hardware  <a name="hardware"></a>
TODO



## Makefile  <a name="makefile"></a>
The file `Makefile` is a very convenient way to execute the different programs to control the beebot.

### Demo mode
Perform coreography on the beebot. The arms and the head should move. Useful to test.
```bash
make run-demo_day
```

### Local execution
Open an SSH session on the beebot and controll it remotely.
```bash
make run-local-client
```
#### Keys <a name="keys"></a>
* CTRL+D: exit the client.
* Arrows: platform (forward, backward, and spin).
* ol kñ: right arm (shoulder, elbow).
* OL KÑ: left arm (shoulder, elbow).
* ws ad: head (tilt, pan).
* c: switch on/off the streaming webcam.
* Space: laser.


### AWS iot execution
This mode allows to controll the beebot through [AWS IoT](https://aws.amazon.com/iot/).

#### Backend
The backend is intended to run on the beebot.
```
make run-aws_iot-backend
```

#### Client
The client can be run in other device that is not the beebot. Please, install the environment in that device (see the installation [document](installation.md#project)).
```
make run-aws_iot-client
```

##### Keys
The AWS IoT client can be controlled [with the same keys](#keys) as the local client.


#### Web client
TODO

#### AWS certificates
The AWS IoT certificates should be in the folders:
* `beebot/data/AWS_iot-beebot`
* `beebot/data/AWS_iot-client`
And the paths can be configured in the files:
* `beebot/beebot/beebot-aws_iot-backend`
* `beebot/beebot/beebot-aws_iot-client`


## Autorun  <a name="autorun"></a>
If you want some behaviour to start everytime you reboot the beebot.
```
apt-get install supervisor
cd
cp beebot/deploy/beebot.conf  /etc/supervisor/conf.d/
```

Edit the `command` section of the file `/etc/supervisor/conf.d/beebot.conf` to choose the behavior.
Example for AWS IoT.
```
command=/home/pi/beebot/beebot/make run-aws_iot-backend
```
