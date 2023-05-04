import requests

from bs4 import BeautifulSoup
import lxml

from fake_useragent import UserAgent
from datetime import datetime
from calendar import monthrange
from pathlib import Path

ua = UserAgent()
ua_ = ua.random


url_ = 'https://www.coincarp.com/currencies/creo-engine/richlist/'

headers = {
    'authority': 'www.nchacutting.com',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6,vi;q=0.5,pt;q=0.4,ka;q=0.3',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': '_gid=GA1.2.42207672.1672040870; _gcl_au=1.1.2090788266.1672040870; _ga_TDHNQ6RXD5=GS1.1.1672142442.3.0.1672142442.0.0.0; _ga=GA1.1.2021857423.1672040869',
    'origin': 'https://www.nchacutting.com',
    'referer': 'https://www.nchacutting.com/ncha-shows/world-standings/show-results',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': f'{ua_}',
    'x-requested-with': 'XMLHttpRequest',
}

with requests.Session() as session:
    response = requests.post(
        f'{url_}',
        headers=headers,
        timeout=(3, 3)
    )

    soup = BeautifulSoup(response.text, 'lxml')

    e_ = soup.find_all('div', class_='address-item')
    for wal_ in e_:
        print(wal_.find('span', class_='mr-2').text)
