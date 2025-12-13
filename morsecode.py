import time
import re

from light import Light


alphabet = {
  'a': '.-',
  'b': '-...',
  'c': '-.-.',
  'ch': '----',
  'd': '-..',
  'e': '.',
  'f': '..-.',
  'g': '--.',
  'h': '....',
  'i': '..',
  'j': '.---',
  'k': '-.-',
  'l': '.-..',
  'm': '--',
  'n': '-.',
  'o': '---',
  'p': '.--.',
  'q': '--.-',
  'r': '.-.',
  's': '...',
  't': '-',
  'u': '..-',
  'v': '...-',
  'w': '.--',
  'x': '-..-',
  'y': '-.--',
  'z': '--..'
}


class InvalidMorseCodeException(Exception):
  """ Exception for if a string does not consist of just dots and dashes """


class MorseCodeFlasher:
  """
  Initialises with an instance of class Light and uses it to flash morse code messages
  when flash_word or flash_code are called
  """

  def __init__(self, a_beat: float, delay_between_letters: float, light: Light):
    self.a_beat = a_beat
    self.delay_between_letters = delay_between_letters
    self.light = light


  def __light_up_for(self, seconds: float):
    self.light.on()
    time.sleep(seconds)
    self.light.off()


  def __dash(self):
    self.__light_up_for(6 * self.a_beat)


  def __dot(self):
    self.__light_up_for(self.a_beat)


  def flash_code(self, code: str):
    """ :param code: A string containing only full-stops (dots) and hypens (dashes) """

    if re.match(r'[^.-]+', code) is not None:
      raise InvalidMorseCodeException

    for flash in code:
      if flash == '.':
        self.__dot()
      elif flash == '-':
        self.__dash()


  def flash_word(self, word: str):
    """ Translates each letter of the word into morse code and passes to flash_code() """
    for letter in word:
      code = alphabet[letter]
      self.flash_code(code)
      time.sleep(self.delay_between_letters)

    self.light.finish()
    print('Done')
