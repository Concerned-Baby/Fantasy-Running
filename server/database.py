import mysql.connector
import logwriter

def start():
	"""
	db = mysql.connector.connect(
		host="localhost",
		user="spinkr",
		password="hi"
		)
	print(db)
	"""
	logwriter.writeServer("Database Started")