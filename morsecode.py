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


class MorseCodeFlasher:
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
    """
    :param code: A string containing only full-stops (dots) and hypens (dashes)
    """

    if re.match(r'[^.-]+', code) is not None:
      raise Exception

    for flash in code:
      if flash == '.':
        self.__dot()
      elif flash == '-':
        self.__dash()


  def flash_word(self, word: str):
    for letter in word:
      code = alphabet[letter]
      self.flash_code(code)
      time.sleep(self.delay_between_letters)
    
    self.light.finish()
    print('Done')
