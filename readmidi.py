from mido import MidiFile, tempo2bpm, tick2second, bpm2tempo
import time
from time import sleep

MidiFile.ticks_per_beat = 192
# bpm = 120
mid = MidiFile('tadow.mp3.mid')
x = 'note_on channel=0 note=51 velocity=67 time=1'
for i, track in enumerate(mid.tracks):
    print('Track{}:{}'.format(i, track.name))
    for msg in track:
        list1 = msg.bytes()
        if tuple(list1)[-2] == 56 and tuple(list1)[-3] == 144:
            print('Motor 1 hit ', msg.time * 0.002604)
            sleep(msg.time * 0.002604)
        elif tuple(list1)[-2] == 56 and tuple(list1)[-3] == 128:
            print('break', msg.time * 0.002604)
            sleep(msg.time * 0.002604)
        else:
            print('idle', msg.time * 0.002604)
            time.sleep(msg.time * 0.002604)
        # print(msg, msg.time * 0.002604)
        # print((tick2second(tick=3, ticks_per_beat=192, tempo=500000)))
        # print(tick2second(tick=3, ticks_per_beat=192, tempo=500000))
        # if msg != msg.is_meta:
        #       if msg != msg.is_meta and msg.type is x:
        #         print(msg)
        # else :
        # print msg...................
