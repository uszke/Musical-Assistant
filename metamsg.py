from mido import MetaMessage, Message, MidiFile, MidiTrack
import time

<<<<<<< HEAD
import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)

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
