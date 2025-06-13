import requests
from bs4 import BeautifulSoup


class SimpleGameParser:
    def __init__(self, url, path):
        self.url = url
        self.path = path
        self.res = []

    def get_html(self):
        req = requests.get(self.url)
        self.html = BeautifulSoup(req.text, "lxml")

    def parsing(self):
        news = self.html.find_all('div', class_='ShelfCard_card__GrWrN')

        for item in news:
            title = item.find('h3', class_='ShelfCard_cardLink__mSxdR').text
            href = item.find('a', class_='ShelfCard_cardLink__mSxdR')['href']
            card = item.find('div', class_='ShelfCard_cardFooter__tkRln').text

            self.res.append({
                "title": title,
                "href": href,
                "card": card


            })

    def save(self):
        with open(self.path, 'w') as f:
            for i, item in enumerate(self.res, 1):
                f.write(
                    f"Новость №{i}\n"
                    f"Заголовок: {item['title']}\n"
                    f"Ссылка: {item['href']}\n"
                   
                    f"Описание: {item['card']}\n"
                    f"{'-' * 50}\n\n"
                )

    def run(self):
        self.get_html()
        self.parsing()
        self.save()