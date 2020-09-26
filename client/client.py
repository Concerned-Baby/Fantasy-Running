import socket
def startClient():
	cs = socket.socket()
	host = socket.gethostname()
	port = 8433
	cs.connect((host, port))
	print(str(cs.recv(1024)))
	cs.close()