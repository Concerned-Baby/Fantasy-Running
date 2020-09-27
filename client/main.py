import client
import logwriter

def main():
	logwriter.writeClient("program started")
	client.startClient()
  
if __name__ == "__main__":
    main()
