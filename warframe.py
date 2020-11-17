# Credits to Pojomi for search function

import urllib.parse as parse
import urllib.request
from urllib.request import urlopen as req_url
import json
import string
import webbrowser

filename = "list.txt"

# Search API for most recent average price scrape
def search(target):
	
	#print("Searching for " + string.capwords(target) + "...")
	main_url = req_url('https://api.warframe.market/v1/items/' + target.replace(' ', '_').lower() + '/statistics')
	
	data = main_url.read()
	parsed = json.loads(data)
	parsed_data = parsed['payload']['statistics_live']['48hours'][-1]['min_price']
	date_time = parsed['payload']['statistics_live']['48hours'][-1]['datetime']

	return(parsed_data, date_time)


def read_list(filename):
	with open (filename, "r") as infile:
		data = infile.readlines()
		for line in data:
			price, time = search(line.strip())
			print(f"{line.strip()}: {price} Platinum")
			

read_list(filename)

