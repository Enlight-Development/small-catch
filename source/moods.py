"""
moods.py: handling of moods
"""

import random
import faces

from machine import I2C, Pin
from machine_i2c_lcd import I2cLcd

DEFAULT_I2C_ADDR = 0x27
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)
lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 4, 20)

current_mood = ""

class moods:
    def __init__(self, points, current_mood)
        points = 0
        current_mood = ""

        self.points = points
        self.current_mood = current_mood

    def set_mood(self, mood):
        if mood == faces.excited:
            self.current_mood = "Excited"
        elif mood == faces.sleepy:
            self.current_mood = "Sleepy"
        elif mood == faces.surprised:
            self.current_mood = "Surprised"
        elif mood == faces.neutral:
            self.current_mood = "Neutral"
        elif mood == faces.happy:
            self.current_mood = "Happy"
        elif mood == faces.crying:
            self.currrent_mood = "Crying"
        elif mood == faces.eating:
            self.current_mood = "Eating"
        elif mood == faces.hangry:
            self.current_mood = "Hangry"
        elif mood == faces.hungry:
            self.current_mood = "Hungry"

    def check_mood(self):
        if self.current_mood == "Excited":
            points = points + 10
            
        elif self.current_mood == "Sleepy":
            # do nothing
        elif self.current_mood == "Surprised":
            points = points + 15
        elif self.current_mood == "Neutral":
            # do nothing
        elif self.current_mood == "Happy":
            points = points + 5
        elif self.current_mood == "Crying":
            points = points - 10

            results = random.randint(1,10)

            if results == "1":
                self.current_mood = "Hangry"
            else:
                self.current_mood = "Crying"

        elif self.current_mood == "Eating":
            points = points + 5
        elif self.current_mood == "Hangry":
            points = points - 15
        elif self.current_mood == "Hungry":
            points = points - 5
            
            results = random.randint(1,10)
            
            if results == "1":
                self.current_mood = "Hangry"
            else:
                self.current_mood = "Crying"
