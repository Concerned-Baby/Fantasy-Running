import datetime
def writeClient(text):
	file = open("../res/Logs/client.txt", "w")
	file.write("[%s] %s" % (str(datetime.datetime.now()), text))