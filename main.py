import requests
from bs4 import BeautifulSoup

url =  "https://usama00004.github.io/portfolio/"

r = requests.get(url)

soup = BeautifulSoup(r.text, "lxml")
print(soup.div)
