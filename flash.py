#!/usr/bin/env python

from cli_light import CLILight
from morsecode import MorseCodeFlasher
import time
from word_of_the_day import send_todays_word


# The length of a beat in seconds
a_beat = .15

delay_between_letters = 8 * a_beat

light = CLILight()
code_flasher = MorseCodeFlasher(a_beat, delay_between_letters, light)

time.sleep(2 * a_beat)

send_todays_word(code_flasher)
