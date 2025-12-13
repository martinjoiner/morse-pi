from datetime import date

from morsecode import MorseCodeFlasher
from words import words


def send_todays_word(code_flasher: MorseCodeFlasher):
  """ Establishes what today's word of the day is and sends to code_flasher """
  today = date.today()
  month = today.strftime("%b")
  day = int(today.strftime("%d"))

  print('Word of the day for ' + str(day) + ' ' + month)

  todays_word = words[month][day-1]
  code_flasher.flash_word(todays_word.lower())
