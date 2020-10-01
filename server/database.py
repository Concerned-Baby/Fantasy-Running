import mysql.connector
import logwriter

def start():
	"""
	db = mysql.connector.connect(
		host="localhost",
		user="skywa",
		password="!Spring18" #its my throwaway password, don't try any shit
		)
	print(db)
	"""
	logwriter.writeServer("Database Started")