import socket
import logwriter
def startServer():
	ss = socket.socket()
	host = socket.gethostname()
	port = 8433
	ss.bind(('',port))
	ss.listen(5)

	print("started server")

	while True:
		client, address = ss.accept()
		print("connection")
		client.send(('thank you for connecting'.encode('utf-8')))
		logwriter.writeServer("Client Accepted: " + address)
		client.close()