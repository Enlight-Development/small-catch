"""
faces.py: All of the faces...
"""

from machine import I2C, Pin
from machine_i2c_lcd import I2cLcd

DEFAULT_I2C_ADDR = 0x27
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)
lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 4, 20)

faces = [
            "(^-^)", # Excited 
            "(-_-)", # Sleepy
            "(o_o)", # Surprised
            "(._.)", # Neutral
            "(0-0)", # Happy
            "(p-p)", # Crying
            "(0o0)", # Eating
            "(-O-)", # Hangry
            "(-.-)"  # Hungry
        ]

excited = faces[0]
sleepy = faces[1]
surprised = faces[2]
neutral = faces[3]
happy = faces[4]
crying = faces[5]
eating = faces[6]
hangry = faces[7]
hungry = faces[8]

# oop!!! 
class faces:
    def __init__(self):
        self.excited = excited
        self.sleepy = sleepy
        self.surprised = surprised
        self.neutral = neutral
        self.happy = happy
        self.crying = crying
        self.eating = eating
        self.hangry = hangry
        self.hungry = hungry

    def set_emotion(emotion):
        lcd.putstr(emotion)