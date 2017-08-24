# beebot
Beebot is a blue robot with pacific intentions.



## Installation

### Operative system

#### Download
Raspbian Jessie Lite
* Minimal image based on Debian Jessie
* Version: January 2017
* Release date: 2017-08-16
* Kernel version: 4.9
* Available at https://downloads.raspberrypi.org/raspbian_lite_latest

#### Copy Raspbian image to the SD card
`dd bs=4M if=2017-08-16-raspbian-jessie-lite.img of=/dev/mmcblk0`


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

#### SSH
By default, Raspbian comes with SSH disabled. It is possible to enable it by running `raspi-config` on a terminal. But since it is a gateway, it does not have a screen nor a keyboard.

See: https://www.raspberrypi.org/blog/a-security-update-for-raspbian-pixel/
>The boot partition on a Pi should be accessible from any machine with an SD card reader, on Windows, Mac, or Linux. If you want to enable SSH, all you need to do is to put a file called ssh in the /boot/ directory. The contents of the file don’t matter: it can contain any text you like, or even nothing at all. When the Pi boots, it looks for this file; if it finds it, it enables SSH and then deletes the file. SSH can still be turned on or off from the Raspberry Pi Configuration application or raspi-config; this is simply an additional way to turn it on if you can’t easily run either of those applications.

_NOTE:_ this is not the previous partition. This is a FAT32 type partition, located in my system as:
`/media/samuelmunoz/boot`

```bash
touch /media/samuelmunoz/boot/ssh
```

### First connection
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

#### Update system
Lets update the system.
```bash
apt-get update
apt-get upgrade
apt-get clean
```

## Streaming webcam

### Installation

### Web Streaming
Command:
```
cvlc --no-audio v4l2:///dev/video0:width=640:height=480 --v4l2-fps 10      --sout "#transcode{vcodec=MJPG,vb=400}:standard{access=http,mux=mpjpeg,dst=:18223/}" --sout-http-mime="multipart/x-mixed-replace;boundary=--7b3cc56e5f51db803f790dad720ed50a"
```
[Sample web](doc/examples/streaming-web.html)



## UV4L


### Installation
See: http://www.linux-projects.org/uv4l/tutorials/
```
curl http://www.linux-projects.org/listing/uv4l_repo/lrkey.asc | sudo apt-key add -
echo "deb http://www.linux-projects.org/listing/uv4l_repo/raspbian/ jessie main" >> /etc/apt/sources.list
apt-get install uv4l uv4l-raspicam uv4l-raspicam-extras
```

### Start service
Configuration file is `/etc/uv4l/uv4l-raspicam.conf`
```
sudo service uv4l_raspicam restart
```
