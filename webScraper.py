"""
beautiful soup 4 tutorial #1 - web scraping with python
tech with tim
"""

from bs4 import BeautifulSoup
import requests

url="https://www.newegg.com/asrock-challenger-rx9070-cl-16g-radeon-rx-9070-16gb-graphics-card-triple-fans/p/N82E16814930138?item=N82E16814930138&cm_sp=homepage_ss-_-p1_14-930-138-_-07302026&source=f"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

# print(doc.prettify())

prices = doc.find_all(string="$")
parent = prices[0].parent
strong = parent.find("strong")
print(strong.string)


