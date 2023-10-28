import os
import csv
from typing import List

import requests
from bs4 import BeautifulSoup

year = 2010
month = 2
day = 3
URL = f"https://www.cbr-xml-daily.ru/archive/{year}/" + str(month).zfill(2) + "/" + str(day).zfill(2) + "/daily_json.js"
print(URL)
html_page = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"})
soup = BeautifulSoup(html_page.text, "lxml")

data = soup.text

index = data.find("USD")
print(index)
true_index_begin = data.find("Value", index)
print(true_index_begin)
true_index_end = data.find(",", true_index_begin)

result=""
for i in range(true_index_begin+6, true_index_end):
    result = result + data[i] 
print("USD value is " + result)