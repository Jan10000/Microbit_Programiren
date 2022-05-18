# Add your Python code here. E.g.
from microbit import *


import random

random = random.randint(("00000:"
              "00000:"
              "00900:"
              "00000:"
              "00000",
              "00000:"
              "00000:"
              "90009:"
              "00000:"
              "00000"))



while True:
    if accelerometer.was_gesture("shake"):
        sleep(1000)
        display.show(random)

















import random

number = random.randint(1,6)


display.show(number)

boat = Image(("00000:"
              "00000:"
              "00900:"
              "00000:"
              "00000"))