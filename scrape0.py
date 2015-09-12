import requests
page = requests.get('http://github.com/zach-king/')
print(page.content)