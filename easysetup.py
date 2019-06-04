from mido import MetaMessage, Message, MidiFile, MidiTrack
import time
from RPi import GPIO
from time import sleep

motor1 = 0
motor2 = 0
note1 = 0
note2 = 0

GPIO.VERBOSE = False
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

name = int(input("How many motors are you using: "))

if name == 1:
    motor1 = 23
    note1 = int(input("What note it refers to: "))
elif name == 2:
    motor1 = 23
    note1 = int(input("What note first motor refers to: "))
    motor2 = 24
    note2 = int(input("What note second motor refers to: "))
else:
    print("I'm just a prototype! Please be easy on me! :( ")

GPIO.setup(motor1, GPIO.OUT)
GPIO.setup(motor2, GPIO.OUT)


def hit_motor1():
    GPIO.output(motor1, GPIO.HIGH)
    sleep(0.07)
    print("ON")
    GPIO.output(motor1, GPIO.LOW)
    sleep(0.5)
    print("OFF")


def hit_motor2():
    GPIO.output(motor2, GPIO.HIGH)
    sleep(0.07)
    print("Second motor ON")
    GPIO.output(motor2, GPIO.LOW)
    sleep(0.5)
    print("Second motor OFF")


mid = MidiFile('tadow.mp3.mid')
for i, track in enumerate(mid.tracks):
    print('Track{}:{}'.format(i, track.name))
    for msg in track:
        list1 = msg.bytes()
        if tuple(list1)[-2] == 26:
            hit_motor1()
            time.sleep(msg.time)
            print('Motor 1 hit ', msg.time)
        if tuple(list1)[-2] == 133:
            hit_motor2()
            time.sleep(msg.time)
            print("Motor 2 hit", msg.time)
