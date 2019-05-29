from mido import MidiFile, tempo2bpm
mid =  MidiFile('tadow.mp3.mid')
char x = 'note_on channel=0 note=51 velocity=67 time=1'
for i, track in enumerate(mid.tracks):
	print('Track{}:{}'.format(i,track.name))
	for msg in track :
	#	if msg != msg.is_meta:
			
		if msg !=msg.is_meta  and  msg.type is x:
			print msg
	#	else :
	#		print msg
         

