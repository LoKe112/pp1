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