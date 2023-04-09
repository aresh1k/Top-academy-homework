import requests
from bs4 import BeautifulSoup


class Parse:

    def __init__(self, html):
        self.urls_list = []
        self.data = ''
        soup_main = BeautifulSoup(html, "lxml")
        ul = soup_main.find('ul', class_='list-tournament row')
        pages = ul.find_all('li', class_='col-sm-6 col-lg-4')
        for page in pages:
            page_url = page.find('div', class_='tournament').find('a').get('href')
            self.urls_list.append('https://cybermos.ru' + page_url)

    @staticmethod
    def get_html(url):
        res = requests.get(url)
        return res.text

    @staticmethod
    def get_data(html):
        soup = BeautifulSoup(html, "lxml")
        div = soup.find('div', class_='turnament')
        name = div.find('div', class_='col-sm').find('h1').text
        date = div.find('div', class_='col-sm').find('div', class_='date').text
        organizer = div.find('div', class_='turnament-manager row').find('div', class_='status').text
        print(name)
        print(date)
        print(organizer)
        return f"Название - {name}; Дата проведения - {date}; Организатор - {organizer}\n"

    def parse_pages(self):
        for page in self.urls_list:
            data = self.get_data(self.get_html(page))
            self.data += data

    def save_data(self):
        with open('f.txt', 'w') as f:
            f.write(self.data)
            print('Данные сохранены в файл')


def main():
    url = 'https://cybermos.ru/tournament/'
    data_parse = Parse(requests.get(url).text)
    data_parse.parse_pages()
    data_parse.save_data()


if __name__ == '__main__':
    main()
