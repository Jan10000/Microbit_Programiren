# Add your Python code here. E.g.
from microbit import *

boat = Image(("00000:"
              "00000:"
              "00900:"
              "00000:"
              "00000"))
while True:
    if accelerometer.was_gesture("shake"):
        sleep(1000)
        display.show(boat)
   