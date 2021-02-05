# LED Morse Code

Python project runs on a Raspberry Pi to flash morse code via a PiBorg LED.

## Installation

sudo apt-get install wiringpi
TODO: Complete this list

## Run

```
sudo ./listen.py
```

## Run automatically on Raspberry Pi Power-on

```
sudo vim /etc/rc.local
```

And add this line before the `exit 0`

```
python /home/pi/morse/morse.py &
```
