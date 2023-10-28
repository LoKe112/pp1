import os
import csv
import time
from typing import List

import requests
from bs4 import BeautifulSoup
result_data = []
for year in range(2008,2024):
    for month in range(1,13):
        for day in range(1,32):
            URL = f"https://www.cbr-xml-daily.ru/archive/{year}/" + str(month).zfill(2) + "/" + str(day).zfill(2) + "/daily_json.js"
            print(URL)
            html_page = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"})
            soup = BeautifulSoup(html_page.text, "lxml")

            data = soup.text
            if "\"error\": \"Not found\"" not in data:

                index = data.find("USD")
                print(index)
                true_index_begin = data.find("Value", index)
                print(true_index_begin)
                true_index_end = data.find(",", true_index_begin)

                result=""
                for i in range(true_index_begin+6, true_index_end):
                    result = result + data[i] 
                print("USD value is " + result)
                result_data.append([str(day).zfill(2)+'.' +
                            str(month).zfill(2)+'.' + str(year),
                            result,])
            else:
                print(f"can not pars{year}.{month}.{day}")

with open("data.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(result_data)

            
                
