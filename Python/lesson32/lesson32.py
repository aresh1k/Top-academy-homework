from bs4 import BeautifulSoup
import requests


def get_html(url):
    res = requests.get(url)
    return res.text


def get_data(html):
    soup = BeautifulSoup(html, "lxml")
    ul = soup.find('ul', class_='list-event-page row')
    news = ul.find_all('li')
    for post in news:
        name = post.find('div', class_='name').find('a').text
        date = post.find('div', class_='event-date').text
        data = {'name': name, 'date': date}
        print(data)


def main():
    url = 'https://cybermos.ru/news/'
    get_data(get_html(url))


if __name__ == '__main__':
    main()
