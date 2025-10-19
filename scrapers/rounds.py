from bs4 import BeautifulSoup
import requests

url = "https://bloons.fandom.com/wiki/Money#Starting_Cash"
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

caption = soup.find("caption")
table = caption.find_parent("table")
tbody = table.find("tbody")

rows = tbody.find_all("tr")
print(rows)

rounds = {}

for row in range(101):
    elements = rows[row].find_all("td")
    if len(elements) == 4:
        rounds[elements[0].text.strip()] = elements[2].text.strip()


