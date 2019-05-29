from mido import MidiFile
mid =  MidiFile('tadow.mp3.mid')

for i, track in enumerate(mid.tracks):
	print('Track{}:{}'.format(i,track.name))
	for msg in track :
		print msg
        tempo2bpm() 

