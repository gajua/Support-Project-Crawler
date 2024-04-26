import re
from time import sleep

from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from bs4 import BeautifulSoup


from news import News


_URL = 'https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do'
_CHROME_DRIVER: Chrome = None


def get_detail_url(id: str):
    return f'https://www.k-startup.go.kr/web/contents/bizpbanc-ongoing.do?schM=view&pbancSn={id}&page=1&schStr=regist&pbancEndYn=N'


def get_current_page_news():
    result: list[News] = []

    # TODO: 뉴스 목록 파싱

    return result


def get_news():
    result: list[News] = []

    # TODO: 크롤링

    return result


def setup_driver():
    global _CHROME_DRIVER

    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--window-size=1920,1080')
    # options.add_argument('--headless')

    service = Service(ChromeDriverManager().install())
    _CHROME_DRIVER = webdriver.Chrome(service=service, options=options)
    _CHROME_DRIVER.implicitly_wait(15)


def main():
    setup_driver()

    result = get_news()

    for news in result:
        print(news)


if __name__ == '__main__':
    main()
