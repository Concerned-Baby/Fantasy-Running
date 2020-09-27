import datetime
def writeServer(text):
	file = open("../res/Logs/server.txt", "w")
	file.write("[%s] %s" % (str(datetime.datetime.now()), text))