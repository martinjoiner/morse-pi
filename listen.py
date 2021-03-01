#!/usr/bin/env python

import time
import wiringpi
from datetime import date
from words import words
from morsecode import alphabet
import requests

wiringpi.wiringPiSetup()

# Setup the LedBorg GPIO pins
PIN_RED = 0
PIN_GREEN = 2
PIN_BLUE = 3
wiringpi.pinMode(PIN_RED, wiringpi.GPIO.OUTPUT)
wiringpi.pinMode(PIN_GREEN, wiringpi.GPIO.OUTPUT)
wiringpi.pinMode(PIN_BLUE, wiringpi.GPIO.OUTPUT)

# Setup the push button GPIO pin
wiringpi.pinMode(6, wiringpi.GPIO.INPUT)


# Set the colour channels (1 is on, 0 is off) and the time delay in seconds
red = 1
green = 1
blue = 1

# The length of a beat
aBeat = .15

delayBetweenLetters = 8 * aBeat

# Set the LedBorg colour
def lightUpFor(seconds):
  wiringpi.digitalWrite(PIN_RED, red)
  wiringpi.digitalWrite(PIN_GREEN, green)
  wiringpi.digitalWrite(PIN_BLUE, blue)

  # Wait for the time delay
  time.sleep(seconds)

  # Turn the LedBorg off
  wiringpi.digitalWrite(PIN_RED, 0)
  wiringpi.digitalWrite(PIN_GREEN, 0)
  wiringpi.digitalWrite(PIN_BLUE, 0)

  time.sleep(aBeat)


def dash():
  lightUpFor(6 * aBeat)


def dot():
  lightUpFor(aBeat)


def sendLetter(letter):
  code = alphabet[letter]
  flashCode(code)


def flashCode(code): 
  for flash in code:
    if flash == '.':
      dot()
    if flash == '-':
      dash()
  time.sleep(delayBetweenLetters)


def sendWord(word):
  for letter in word:
    sendLetter(letter)
  print('Done')  


def sendTodaysWord():
  today = date.today()
  month = today.strftime("%b")
  day = int(today.strftime("%d"))

  print('Today is day ' + str(day))
  todaysWord = words[month][day-1]
  sendWord(todaysWord)


def recordPing():
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
  except:
    print('Post failed')


flashCode('-.-')
print("Listening for button...")
while True: # Run forever
  if wiringpi.digitalRead(6):
    print("Button was pushed!")
    time.sleep(2 * aBeat)
    sendTodaysWord()
    recordPing()

