# Add your Python code here. E.g.
from microbit import *

import random

number = random.randint(1,6)

while True:
    display.scroll(number)
