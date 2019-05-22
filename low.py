import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

while True:
    GPIO.output(23, GPIO.HIGH)
    GPIO.output(24, GPIO.HIGH)
    sleep(1)
    print ("ON")
    GPIO.output(23, GPIO.LOW)
    GPIO.output(24, GPIO.LOW)
    sleep(1)
    print("OFF")