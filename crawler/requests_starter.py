import csv

from requests import get
from bs4 import BeautifulSoup


from news import News


_BASE_URL = 'https://www.bizinfo.go.kr/web/lay1/bbs/S1T122C128/AS/74/'
_URL = f'{_BASE_URL}list.do?rows=15&cpage=1'


def get_news():
    result: list[News] = []
    # 뉴스 정보를 가져온다
    response = get(_URL).text
    bs4object = BeautifulSoup(response, 'html.parser')

    div = bs4object.find('div', {'class': "table_Type_1"})
    tbody = div.find('tbody')
    tr_list = tbody.find_all('tr')

    for tr in tr_list:
        a_tag: BeautifulSoup = tr.find('a')
        title = a_tag.get_text().strip()
        href = a_tag['href']

        url = f'{_BASE_URL}{href}'
        # String Interpolation
        news = News(url=url, title=title)
        result.append(news)

    # TODO: 크롤링

    return result


def main():
    result = get_news()

    with open('news.csv', 'w') as file:
        writer = csv.writer(file)

        for _, news in enumerate(result):
            writer.writerow([news.title, news.url])
            # print(f'url: {news.url}, title: {news.title}')
            # print(news)
            # res = f'url: {news.url}, title: {news.title}'

            # if index < len(result) - 1:
            #     res += '\n'

            # file.write(res)


        file.close()


if __name__ == '__main__':
    main()
