
import random
import json
import machine
import utime
import requests
from time import sleep_ms, ticks_ms
import network
import socket
from time import sleep
import threading
from machine import I2C, Pin
from machine_i2c_lcd import I2cLcd
DEFAULT_I2C_ADDR = 0x3F
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)
lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16)

led_onboard = machine.Pin("LED", machine.Pin.OUT)



clients = "000"

def ledon():
    led_onboard.value(1)
    
def ledoff():
    led_onboard.value(0)

def randomname():
    with open("names.txt") as f:
        lines = f.readlines()
    return random.choice(lines)



temp = "Welcome To"
lcd.move_to(3,0)
for char in temp:
    lcd.putstr(char)
    sleep(.2)
    



lcd.blink_cursor_off()
lcd.hide_cursor()
lcd.move_to(2,1)
temp = "Small Catch."
for char in temp:
    lcd.putstr(char)
    sleep(.2)
  
sleep(3) 
lcd.clear()
lcd.move_to(0,0)
lcd.putstr(f"(-_-)")
ledoff()
sleep(1)
lcd.clear()
lcd.putstr("(~_~)")
ledon()
sleep(.34)
lcd.clear()
lcd.putstr("(-_-)")
ledoff()
sleep(.45)
lcd.clear()
lcd.putstr("(~_~)")
ledon()
sleep(.5)
lcd.clear()
lcd.putstr("(o_o)")
sleep(.3)
lcd.clear()
ledoff()


        
ap = network.WLAN(network.AP_IF)
ap.config(essid="a")
ap.active(True)
    

lcd.putstr(f"(._.)   CLI: {clients}")
lcd.move_to(0,1)
lcd.putstr(f"BTE: 1 WIFI: 1") # not fixated
    


