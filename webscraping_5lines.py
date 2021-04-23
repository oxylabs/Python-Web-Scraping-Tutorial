import requests
from bs4 import BeautifulSoup
response = requests.get("https://en.wikipedia.org/wiki/Web_scraping")
bs = BeautifulSoup(response.text, "lxml")
print(bs.find("p").text)
