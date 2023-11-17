from func import *


def main() -> None:
    result_data = []
    for year in range(2008, 2024):
        for month in range(1, 13):
            for day in range(1, 32):
                URL = (
                    f"https://www.cbr-xml-daily.ru/archive/{year}/"
                    + str(month).zfill(2)
                    + "/"
                    + str(day).zfill(2)
                    + "/daily_json.js"
                )
                print(URL)
                html_page = requests.get(
                    URL, headers={"User-Agent": "Mozilla/5.0"})
                soup = BeautifulSoup(html_page.text, "lxml")

                data = soup.text
                true_index_search(day, month, year, data, result_data)

    csv_write(result_data)
