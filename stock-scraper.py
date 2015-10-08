"""
File: gov-bills-scraper.py
Author: Zachary King
Description: A web scraper that retrieves the 
	stock value for a given list of companies 
	(by symbols), and plots the values on a 
	bar graph accordingly, with color-coding. 
"""

import requests
import time
from bs4 import BeautifulSoup
import numpy as np
import matplotlib.pyplot as plt

start_time = time.time()

# Variable declarations
symbols = ["aapl", "goog", "msft", "yhoo", "amzn", "fb", "twtr", "nflx"]
numCompanies = len(symbols)
values = []
arrows = []

# Scrape the data
for s in symbols:
	url = "http://finance.yahoo.com/q?&s=" + s
	r = requests.get(url)
	soup = BeautifulSoup(r.content)
	price = soup.find_all("span", {"id": "yfs_l84_"+s})
	arrow = soup.find_all("span", {"id": "yfs_c63_"+s})
	arrows.append(arrow[0].next_element["class"])
	print(s.upper() + " share value: $" + price[0].text)
	values.append(price[0].text)
	symbols[symbols.index(s)] = symbols[symbols.index(s)].upper()

# convert values from strings to floats
for i in range(numCompanies):
	values[i] = float(values[i])

# Plot and figure
fig = plt.figure()
fig.canvas.set_window_title('Stock-Scraper')
ax = fig.add_subplot(111)

index = np.arange(numCompanies)
rects = ax.bar(index, values, 0.25, alpha=0.5)

# Show the number value for the share above the bar
for i in range(numCompanies):
	ax.annotate('$' + str(values[i]), xy=(i+0.12, values[i]), xytext=(i - 0.12, values[i] + 10),
            arrowprops=dict(arrowstyle='-'),
            )

# Labels and titles on graph
plt.xlabel('Company')
plt.ylabel('Share Value')
plt.title('Current Share Value for Companies')
plt.xticks(index + 0.25, symbols)

# Color the bars based on the companies' stock status
for i, arrow in enumerate(arrows):
	if (arrow == [u'pos_arrow']):
		rects[i].set_color('g') # stock is going up
	elif (arrow == [u'neg_arrow']):
		rects[i].set_color('r') # stock is going down
	else:
		rects[i].set_color('b') # unknown data

print("--- %s seconds ---" % (time.time() - start_time))

# Show the graph
fig.tight_layout()
plt.show()
