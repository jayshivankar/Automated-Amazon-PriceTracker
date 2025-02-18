import requests
from bs4 import BeautifulSoup

URL="https://appbrewery.github.io/instant_pot/"
response=requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')
o_price=soup.find(class_="a-offscreen")
price=o_price.text.split("$")[1]


