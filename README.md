# LED Morse Code

Python project that runs on a Raspberry Pi with an PiBorg LED to flash the word-of-the-day in morse code when a button is pushed.

- `listen.py` - Endless command to listen for button-push on Raspberry Pi
- `flash.py` - Command-line mode that doesn't require PiBorg LED for debugging

## Installation on Raspberry Pi

sudo apt-get install wiringpi
TODO: Complete this list

Copy the example library of words...

```
cp words.example.py words.py
```

...and then populate with the secret values.

## Run on Raspberry Pi

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
