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

=======
mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

track.append(Message('program_change', program=12, time=0))
track.append(Message('note_on', note=30, velocity=64, time=0))
track.append(Message('note_off', note=30, velocity=127, time=60))
track.append(Message('note_on', note=70, velocity=64, time=120))
track.append(Message('note_off', note=70, velocity=127, time=120))
track.append(Message('note_on', note=65, velocity=64, time=180))
track.append(Message('note_off', note=65, velocity=127, time=240))

mid.save('tests.mid')

for i, track in enumerate(mid.tracks):
    print('Track{}:{}'.format(i, track.name))
    for msg in track:
        # if msg == 'note=30, velocity=127, time=60':
        #	print(msg)
        # if msg.is_meta :
        # print(msg.bytes())
        # L = msg.bytes()
        print(msg.bytes()[2:])
>>>>>>> 7e428f6dd71d8c221e4f0e221ee09bed517bf8df
