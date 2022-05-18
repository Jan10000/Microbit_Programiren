# Add your Python code here. E.g.
from microbit import *

jocker= Image("90009:"
              "00000:"
              "90009:"
              "00000:"
              "90009")

while True:
    if button_a.is_pressed():
        display.show(jocker)

