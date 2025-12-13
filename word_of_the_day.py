from datetime import date

from light import Light
from morsecode import MorseCodeFlasher
from words import words


def send_todays_word(code_flasher: MorseCodeFlasher):
  today = date.today()
  month = today.strftime("%b")
  day = int(today.strftime("%d"))

  print('Word of the day for ' + str(day) + ' ' + month)

  todays_word = words[month][day-1]
  code_flasher.flash_word(todays_word.lower())
