import Adafruit_BBIO.PWM as PWM
import Adafruit_BBIO.GPIO as GPIO 
from subprocess import call 
import time
#import datetime
import os 
import Adafruit_CharLCD as LCD
from multiprocessing import Process
import sys
import thread

PWM.start("P9_14", 50, 1000, 1)
PWM.set_frequency("P9_14", 2000)
PWM.set_duty_cycle("P9_14", 100)

# BeagleBone Black configuration:
lcd_rs        = 'P8_8'
lcd_en        = 'P8_10'
lcd_d4        = 'P8_18'
lcd_d5        = 'P8_16'
lcd_d6        = 'P8_14'
lcd_d7        = 'P8_12'
lcd_backlight = 'P8_7'

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows    = 2

a = 1

# Initialize the LCD using the pins above.
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, 
lcd_columns, lcd_rows, lcd_backlight)

def speak(user_input):
    call(["flite", "-voice", "rms", "-t", user_input])

def powerup():
    PWM.set_duty_cycle("P9_14", 0)
    time.sleep(0.02)
    PWM.set_duty_cycle("P9_14", 10)
    time.sleep(0.02)
    PWM.set_duty_cycle("P9_14", 20)
    time.sleep(0.02)
    PWM.set_duty_cycle("P9_14", 30)
    time.sleep(0.02)
    PWM.set_duty_cycle("P9_14", 40)
    time.sleep(0.02)
    PWM.set_duty_cycle("P9_14", 50)
    time.sleep(0.02)
    PWM.set_duty_cycle("P9_14", 60)
    time.sleep(0.02)
    PWM.set_duty_cycle("P9_14", 70)
    time.sleep(0.02)
    PWM.set_duty_cycle("P9_14", 80)

# Print a two line message
lcd.message('Debian Booted')
speak('debian booted')

time.sleep(4.0)
lcd.clear()

lcd.message('Enabling\nBlaster...')
speak('enabling blaster')
time.sleep(2.0)

PWM.set_duty_cycle("P9_14", 90)
time.sleep(0.2)
PWM.set_duty_cycle("P9_14", 30)
time.sleep(0.2)
PWM.set_duty_cycle("P9_14", 90)
time.sleep(0.4)
call(['aplay','PowerUp.wav'])
PWM.set_duty_cycle("P9_14", 80)

lcd.clear()

lcd.message('Boot\nComplete!')
speak('Power up complete')
GPIO.setup("P9_11", GPIO.IN)
debounce = 0

time.sleep(1)
lcd.clear()



#MAIN LOOP
while a == 1:

   # now = datetime.datetime.now()

    #lcd.clear()
    #lcd.message("Current Time:\n"+now.strftime("%H:%M")
    
    b = GPIO.input("P9_11")

    if b == 1:
         if debounce == 0:
             PWM.set_duty_cycle("P9_14", 0)
             call(['aplay','GunFire.wav'])
             powerup()
             debounce = 1
         debounce = 0
    else: 
         PWM.set_duty_cycle("P9_14", 80)

