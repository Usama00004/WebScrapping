import requests
from bs4 import BeautifulSoup
import re
url =  "https://usama00004.github.io/portfolio/"

r = requests.get(url)

soup = BeautifulSoup(r.text, "lxml")

print(soup.div)

# Regular Expressions
# data = soup.find_all(string= re.compile("string_to_find"))

