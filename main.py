import requests
from bs4 import BeautifulSoup


def get_html(url):
    try:
        response = requests.get(url=url)
        with open("/home/maxim/Project/parser_av/data_html.html", "w") as file:
            file.write(response.text)
    except Exception:
        print("Ошибка сайта")


def get_data():
    quantity = 1
    data = {}
    with open("/home/maxim/Project/parser_av/data_html.html") as file:
        str_html = file.read()
    soup = BeautifulSoup(str_html, "lxml")
    for listing_item in soup.find_all(class_='listing-item'):
        print("quantity == ",quantity)
        data["Name"] = listing_item.find(class_="link-text").text
        data["Location"] = listing_item.find(class_="listing-item__location").text
        data["Date"] = listing_item.find(class_="listing-item__date").text
        str_param = listing_item.find(class_="listing-item__params").text
        sedan_index = str_param.find('седан')
        sedan_len = len('седан')
        str_param = str_param[:sedan_index + sedan_len] + ", " + str_param[sedan_index + sedan_len:]
        str_param = str_param[:6] + ", " + str_param[7:]
        data["Params"] = str_param
        data["Price"] = listing_item.find(class_="listing-item__price").text

        for key, value in data.items():
            print(f"{key}: {value}")
        print("\n")
        quantity += 1


def main():
    for i in range(1, 4):
        url = f'https://cars.av.by/filter?brands[0][brand]=683&brands[0][model]=5897&brands[0]' \
              f'[generation]=4615&page={i}&sort=3'
        get_html(url)
        get_data()


if __name__ == "__main__":
    main()