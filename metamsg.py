from mido import MetaMessage, Message, MidiFile, MidiTrack

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
