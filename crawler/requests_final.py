from requests import get
from bs4 import BeautifulSoup


from news import News


_BASE_URL = 'https://www.bizinfo.go.kr/web/lay1/bbs/S1T122C128/AS/74/'
_URL = f'{_BASE_URL}list.do?rows=15&cpage=1'


def get_news():
    result: list[News] = []

    res = get(url=_URL).text
    bs4obj = BeautifulSoup(res, 'html.parser')

    tr_list = bs4obj.find('div', {'class': 'table_Type_1'}).find(
        'tbody').find_all('tr')

    for tr in tr_list:
        td_list = tr.find_all('td')
        title = td_list[2].get_text().strip()
        href = tr.find('a')['href']
        url = f'{_BASE_URL}{href}'

        news = News(url=url,
                    title=title)
        result.append(news)

    return result


def main():
    result = get_news()

    for news in result:
        print(news)


if __name__ == '__main__':
    main()
