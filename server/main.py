import database
import server
import logwriter
"""
add log
"""

def main():
	logwriter.writeServer("program started")
	database.start()
	server.startServer()

if __name__ == "__main__":
	main()