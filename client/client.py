import socket
import logwriter
def startClient():
	cs = socket.socket()
	host = socket.gethostname()
	port = 8433
	logwriter.writeClient("Attempting to connect . . . " + host + " : " + port)
	cs.connect((host, port))
	logwriter.writeClient("Connected")
	print(str(cs.recv(1024)))
	cs.close()