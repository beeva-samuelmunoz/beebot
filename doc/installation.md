# Beebot Installation

## Table of contents
* [SD operative]("#sd_operative")
* [First connection]("#first_connection")
* [Project]("#project")

## SD Operative  <a name="sd_operative"></a>

### Operative system

#### Download
Raspbian Stretch Lite
* Minimal image based on Debian Stretch
* Version: January 2017
* Release date: 2017-08-16
* Kernel version: 4.9
* Available at https://downloads.raspberrypi.org/raspbian_lite_latest

#### Copy Raspbian image to the SD card
```bash
dd bs=4M if=2017-08-16-raspbian-stretch-lite.img of=/dev/mmcblk0
```

### Configuration

#### Hostname
Set the name of your device in the file `etc/hostname`.
_Note: do **NOT** use `/etc/hostname`. That is your machine!_
```bash
echo "beebot" > etc/hostname
```

#### WiFi Network (optional)
```bash
nano etc/wpa_supplicant/wpa_supplicant.conf
```
And add a configuration like this.

```
network={
 ssid="YOUR_NETWORK_NAME"
 psk="YOUR_NETWORK_PASSWORD"
 proto=RSN
 key_mgmt=WPA-PSK
 pairwise=CCMP
 auth_alg=OPEN
}
```

#### Camera
Load the camera module on boot up.
```bash
echo "bcm2835-v4l2" >> etc/modules
```



#### SSH
By default, Raspbian comes with SSH disabled. It is possible to enable it by running `raspi-config` on a terminal. But since it is a gateway, it does not have a screen nor a keyboard.

See: https://www.raspberrypi.org/blog/a-security-update-for-raspbian-pixel/
>The boot partition on a Pi should be accessible from any machine with an SD card reader, on Windows, Mac, or Linux. If you want to enable SSH, all you need to do is to put a file called ssh in the /boot/ directory. The contents of the file don’t matter: it can contain any text you like, or even nothing at all. When the Pi boots, it looks for this file; if it finds it, it enables SSH and then deletes the file. SSH can still be turned on or off from the Raspberry Pi Configuration application or raspi-config; this is simply an additional way to turn it on if you can’t easily run either of those applications.

_NOTE:_ this is not the previous partition. This is a FAT32 type partition, located in my system as:
`/media/samuelmunoz/boot`

```bash
touch /media/samuelmunoz/boot/ssh
```



## First connection <a name="first_connection"></a>
At this point, unmount the SD card, plug it into the Raspberry and wait 2 minutes or so to give it time to boot up and connect to the WiFi network.
If everything goes well, you should be able to connect to the device.
```bash
ssh pi@beebot.local
```
_NOTE: the default password is **raspberry**._

#### Change the default passwords
It is highly insecure to leave a gateway with the default password. Change it!
```bash
passwd
```

#### Packages
Update the system.
```bash
apt-get update
apt-get upgrade
apt-get clean
```

Install the required packages.
```
apt-get install python3.5 python3.5-dev virtualenv git vlc
```

#### Camera
Enable the Camera
```bash
raspi-conf
```
Choose `5 Interfacing Options > P1 Camera > Yes` and reboot the system.


And the system is already installed and configured.


## Project <a name="project"></a>
### Clone the project
```bash
cd
git clone https://github.com/beeva-samuelmunoz/beebot.git
```

### Install the environment
```bash
cd beebot
make install-env
```

### Test
Perform a test on the beebot. The arms and the head should move.
```bash
make run-demo_day
```
