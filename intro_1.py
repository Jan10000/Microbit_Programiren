# Add your Python code here. E.g.
from microbit import *

bilder = [Image.DUCK, Image.ANGRY]
zahlen = ["1","2","3"]

while True:
    for z in zahlen:
        display.scroll(z)
    display.scroll("STOP")