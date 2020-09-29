import mysql.connector
import logwriter

def start():
	"""
	db = mysql.connector.connect(
		host="localhost",
		user="skywa",
		password="spinkr"
		)
	print(db)
	"""
	logwriter.writeServer("Database Started")