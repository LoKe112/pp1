
import os
import csv
import time
from typing import List

import requests
from bs4 import BeautifulSoup


def true_index_search(day: str, month: str, year: str, data: str, result_data: str) -> None:
    if '"error": "Not found"' not in data:

        index = data.find("USD")
        true_index_begin = data.find("Value", index)
        true_index_end = data.find(",", true_index_begin)
        result = ""
        for i in range(true_index_begin + 8, true_index_end):
            result = result + data[i]
        print("USD value is " + result)
        result_data.append(
            [
                str(day).zfill(2) + "." +
                str(month).zfill(2) + "." + str(year),
                result,
            ]
        )
    else:
        print(f"can not pars{year}.{month}.{day}")


def csv_write(result_data: str) -> None:
    with open("data.csv", "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(result_data)
