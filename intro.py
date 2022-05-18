# Add your Python code here. E.g.
from microbit import *


while True:
    display.scroll('JAN :')
    sleep(1000)
    display.scroll("HALLO WIE GETS?")
    display.show(Image.DUCK)
    sleep(3000)
    display.scroll("DAS WAR EINE ENTE")
    sleep(2000)
    display.show(Image.GIRAFFE)
    sleep(5000)
    display.scroll("DAS WAR EINE GIRAFE")
    sleep(2000)
    display.show("10 9 8 7 6 5 4 3 2 1 0")
    