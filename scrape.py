import requests

def work():
	URL = 'https://www.athletic.net/TrackAndField/SchoolRecords.aspx?SchoolID=1096'
	page = requests.get(URL)
	print (type(page.content))
	file = open("output.html", "w")
	file.write(str(page.content))