from mido import MetaMessage, Message, MidiFile, MidiTrack


mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

track.append(Message('program_change', program=12, time=0))
track.append(Message('note_on', note=65, velocity=64, time=32))
track.append(Message('note_off', note=65, velocity=127, time=32))

mid.save('ceva.mid')


for i, track in enumerate(mid.tracks):
	print('Track{}:{}'.format(i,track.name))
	for msg in track:
		print(msg)




