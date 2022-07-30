import requests
from bs4 import BeautifulSoup

URL = 'https://cars.av.by/filter?brands[0][brand]=683&brands[0][model]=5897&brands[0][generation]=4615&sort=3'


def get_html(url):
    try:
        response = requests.get(url=URL)
        with open("/home/maxim/Project/parser_av/data_html.html", "w") as file:
            file.write(response.text)
    except Exception:
        print(response.status_code)


def main():
    get_html(URL)


if __name__ == "__main__":
    main()