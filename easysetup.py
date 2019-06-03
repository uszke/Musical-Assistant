from mido import MetaMessage, Message, MidiFile, MidiTrack
import time
from RPi import GPIO
from time import sleep

GPIO.VERBOSE = False
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

name = str(input("How many motors are you using: "))

if name == 1:
    motor1 = 23
    note1 = str(input("What note it refers to: "))
elif name == 2:
    motor2 = 24
    note2 = str(input("What note second motor refers to: "))
else:
    print("I'm just a prototype! Please be easy on me! :( ")

GPIO.setup(motor1, GPIO.OUT)
GPIO.setup(motor2, GPIO,OUT)


def hit():
    GPIO.output(23, GPIO.HIGH)
    sleep(0.07)
    print("ON")
    GPIO.output(23, GPIO.LOW)
    sleep(0.5)
    print("OFF")


mid = MidiFile('tadow.mp3.mid')
for i, track in enumerate(mid.tracks):
    print('Track{}:{}'.format(i, track.name))
    for msg in track:
        list = msg.bytes()
        if tuple(list)[-2] == 26:
            hit()
            time.sleep(msg.time)
            print('hit', msg.time)