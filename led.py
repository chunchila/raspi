import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(True)
GPIO.setup(18,GPIO.OUT)
for x in range(10):
    print "LED on"
    GPIO.output(18,GPIO.HIGH)
    time.sleep(2)
    print "LED off"
    GPIO.output(18,GPIO.LOW)
    time.sleep(2)

