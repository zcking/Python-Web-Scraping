# Python Web Scraping
This repository is home to many of my Python web scraping files. 
I use BeautifulSoup4 (bs4) for all my scraping projects since 
it is easier and cleaner than using regular expressions. I 
usually use *urlopen* to get the web page content and then 
create a "soup" object from there with bs4.

## Installing BeautifulSoup4
Using pip
```
pip install beautifulsoup4
```

Using easy_install
```
easy_install beautifulsoup4
```

### Installing for Linux Users
```
sudo apt-get python-bs4
```

## Python 2.x and 3.x Support of *urlopen()*
To support Python 2.x you simply need to use the import line 
```
from urllib2 import urlopen
```
And for Python 3.x you would use this line instead
```
from urllib.request import urllopen
```
