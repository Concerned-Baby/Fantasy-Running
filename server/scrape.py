import requests
from bs4 import BeautifulSoup

def work():
	URL = 'https://www.athletic.net/TrackAndField/SchoolRecords.aspx?SchoolID=1096'
	page = requests.get(URL)
	print (type(page.content))
	file = open("output.html", "w")
	soup = BeautifulSoup(page.content, 'html.parser')
	file.write(str(soup))