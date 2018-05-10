#! -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

URL = 'https://www.mizuhobank.co.jp/retail/takarakuji/numbers/numbers3/index.html'
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html.parser')
# aタグの取得
print(soup.get("a"))
# 整形後のhtml表示
print(soup.prettify())