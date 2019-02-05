#!/usr/bin/env python

# Tripwire met laser module en lichtsensor
# https://raspberrytips.nl/tripwire-laser

from datetime import datetime
import RPi.GPIO as GPIO
import os, time

SensorGPIO = 23
LaserGPIO = 17

def callback_func(channel):
    if GPIO.input(channel):
        print("Laser onderbroken -> "+str(datetime.now()))

if __name__ == '__main__':

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    # activeer laser

    GPIO.setup(LaserGPIO, GPIO.OUT)
    GPIO.output(LaserGPIO, GPIO.HIGH)

    #setup de lichtsensor
    
    GPIO.setup(SensorGPIO, GPIO.IN)
    GPIO.add_event_detect(SensorGPIO, GPIO.RISING, callback=callback_func, bouncetime=200)

    try:
        while True:
            time.sleep(0.5)
    except:
        GPIO.remove_event_detect(SensorGPIO)
        GPIO.output(LaserGPIO, GPIO.LOW)
        GPIO.cleanup()