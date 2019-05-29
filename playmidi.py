from mido.sockets import PortServer, connect

for msg in PortServer('localhost', 8000):
	for i, track in enumerate(mid.tracks):
		print('Track{}:{}'.format(i,track.name))
	for msg in track:
		print(msg)
	


#output = connect('localhost', 8000):
#output.send(msg)
