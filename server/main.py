import database
import server
"""
add log
"""

def main():
	print("started")
	database.start()
	server.startServer()

if __name__ == "__main__":
	main()