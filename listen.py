#!/usr/bin/env python

import time
import requests

import wiringpi

from light import Light
from morsecode import MorseCodeFlasher
from word_of_the_day import send_todays_word

wiringpi.wiringPiSetup()

# Setup the LedBorg GPIO pins
PIN_RED = 0
PIN_GREEN = 2
PIN_BLUE = 3
wiringpi.pinMode(PIN_RED, wiringpi.GPIO.OUTPUT)
wiringpi.pinMode(PIN_GREEN, wiringpi.GPIO.OUTPUT)
wiringpi.pinMode(PIN_BLUE, wiringpi.GPIO.OUTPUT)

# Setup the push button GPIO pin
PIN_BUTTON = 6
wiringpi.pinMode(PIN_BUTTON, wiringpi.GPIO.INPUT)

# The length of a beat in seconds
A_BEAT = .15

DELAY_BETWEEN_LETTERS = 8 * A_BEAT


class PiBorgLight(Light):
  """ Controls the illumination of PiBorg LED """

  # Set the colour channel intensity (1 is fully on, 0 is off)
  red = 1
  green = 1
  blue = 1


  def on(self):
    """ Turn the LedBorg on """
    wiringpi.digitalWrite(PIN_RED, self.red)
    wiringpi.digitalWrite(PIN_GREEN, self.green)
    wiringpi.digitalWrite(PIN_BLUE, self.blue)


  def off(self):
    """ Turn the LedBorg off """
    wiringpi.digitalWrite(PIN_RED, 0)
    wiringpi.digitalWrite(PIN_GREEN, 0)
    wiringpi.digitalWrite(PIN_BLUE, 0)


light = PiBorgLight()
code_flasher = MorseCodeFlasher(A_BEAT, DELAY_BETWEEN_LETTERS, light)


def record_push():
  """ Makes a HTTP Request to record the event of a button push """
  url = 'http://morse.pelmo.uk/ping/index.php'
  headers = {
    'Content-Type': 'multipart/form-data',
    'User-Agent': 'Morse code RaspberryPi'
  }
  try:
    response = requests.post(url,
      headers=headers,
      data={ 'ping': 1 },
      timeout=3
    )
    print('Response code: ' + str(response.status_code))
  except requests.exceptions.HTTPError as errh:
    print("HTTP Error")
    print(errh.args[0])


code_flasher.flash_code('-.-')

print("Listening for button...")

while True: # Run forever
  if wiringpi.digitalRead(PIN_BUTTON):
    print("Button was pushed!")
    time.sleep(2 * A_BEAT)
    send_todays_word(code_flasher)
    # record_push()
