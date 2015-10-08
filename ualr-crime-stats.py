"""
File: ualr-crime-stats.py
Author: Zachary King
Date Created: 10/7/2015
"""

import requests
from bs4 import BeautifulSoup

alphabet = "abcdefghijklmnopqrstuvwxyz"
url = "http://ualr.edu/safety/home/campus-safety-links/crime-statistics/"
r = requests.get(url)
soup = BeautifulSoup(r.content)

offenses = []

# Get the first table (Crime Statistics for UALR Main Campus)
with open("crime-stats-output.txt", 'w') as f:
	main_campus = soup.find_all("table")[0]
	f.write(main_campus.text)

	# for table in soup.find_all("table"):
	# 	f.write(table.text)
	# 	f.write("--------------------------------------")