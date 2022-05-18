# Add your Python code here. E.g.
from microbit import *
import random

jocker= Image("90009:"
              "00000:"
              "90009:"
              "00000:"
              "90009")


eins = Image("00000:"
             "00000:"
             "00900:"
             "00000:"
             "00000:")

zwei = Image("00000:"
             "00000:"
             "90009:"
             "00000:"
             "00000:")

drei = Image("00009:"
             "00000:"
             "00900:"
             "00000:"
             "90000:")

vier = Image("90009:"
             "00000:"
             "00000:"
             "00000:"
             "90009:")

fünf = Image("90009:"
             "00000:"
             "00900:"
             "00000:"
             "90009:")

sechs = Image("90009:"
              "00000:"
              "90009:"
              "00000:"
              "90009:")
while True:
    if accelerometer.was_gesture("shake"):
        zufall = random.randint(1,6)
        if zufall == 3:
            display.show(drei)
            sleep(2264)
        elif zufall == 2:
            display.show(zwei)
            sleep(2264)
        elif zufall== 6:
            display.show(sechs)
            sleep(2264)
        elif zufall== 4:
            display.show(vier)
            sleep(2264)
        elif zufall== 5:
            display.show(fünf)
            sleep(2264)
        elif zufall== 1:
            display.show(eins)
            sleep(2264)
    elif button_a.is_pressed():
        display.show(jocker)
