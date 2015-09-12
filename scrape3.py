import bs4
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "http://thomaswallace.net/courses/internet-technologies/fall-2015/"
content = urlopen(url).read()

soup = BeautifulSoup(content)

for post in soup.find_all("article", {"class":"post"}):
	children = post.children
	for child in children:
		print(child)
	print("\n")