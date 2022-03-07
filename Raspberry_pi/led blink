import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(2,GPIO.OUT)
GPIO.setup(3,GPIO.OUT)
while True:
    GPIO.output(2,GPIO.HIGH)
    GPIO.output(3,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(2,GPIO.LOW)
    GPIO.output(3,GPIO.LOW)
    time.sleep(0.5)

