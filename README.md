# LED Morse Code

Python project runs on a Raspberry Pi to flash a word-of-the-day in morse code via a PiBorg LED.

## Installation

sudo apt-get install wiringpi
TODO: Complete this list

Copy the example library of words...

```
cp words.example.py words.py
```

...and then populate with the secret values.

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
