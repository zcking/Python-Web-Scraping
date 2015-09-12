from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "http://www.thomaswallace.net"
content = urlopen(url).read()
print(content)

soup = BeautifulSoup(content)

print(soup.prettify())
print(soup.title)
print(soup.title.string)
print(soup.p)
print(soup.a)