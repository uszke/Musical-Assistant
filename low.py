import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

while True:
    GPIO.output(23, GPIO.HIGH)
    sleep(0.08)
    print ("ON")
    GPIO.output(23, GPIO.LOW)
    sleep(0.5)
    print("OFF")
    GPIO.output(23, GPIO.HIGH)
    sleep(0.08)
    print ("ON")
    GPIO.output(23, GPIO.LOW)
    sleep(1)
    GPIO.output(23, GPIO.HIGH)
    sleep(0.08)
    GPIO.output(23, GPIO.LOW)
    sleep(1)
    GPIO.output(23, GPIO.HIGH)
    sleep(0.08)
    GPIO.output(23, GPIO.LOW)
    sleep(1.5)