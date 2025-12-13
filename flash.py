#!/usr/bin/env python

import time

from cli_light import CLILight
from morsecode import MorseCodeFlasher
from word_of_the_day import send_todays_word


# The length of a beat in seconds
A_BEAT = .15

DELAY_BETWEEN_LETTERS = 8 * A_BEAT

light = CLILight()
code_flasher = MorseCodeFlasher(A_BEAT, DELAY_BETWEEN_LETTERS, light)

time.sleep(2 * A_BEAT)

send_todays_word(code_flasher)
