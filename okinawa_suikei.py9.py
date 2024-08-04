# 24010
# 沖縄県の推計人口ページより最新情報をスクレイピングするPythonコード
# https://www.pref.okinawa.jp/toukeika/estimates/estsimates_suikei.html

import requests
from bs4 import BeautifulSoup
uri = 'https://www.pref.okinawa.jp/toukeika/estimates/estimates_suikei.html'
html = requests.get(uri)

# 文字コードをShift_JISにエンコーディング
html.encoding = 'Shift_JIS'

# print(html.text)

# 課題文を読んでコードの続きを作成してみましょう
# これまでに習ったfor、if、リストの操作、文字列の操作をうまく活用して作成しましょう。
# 「HTMLを取得しよう - Python実践編」を参考にしながらコードを作成しましょう

soup = BeautifulSoup(html.text, 'html.parser')
baseElement = soup.find('table', class_='table1 font2 gyo5')

jinkou = [
  "",
  "",
  "",
  ""
]

for i, element in enumerate(baseElement.find_all("td", align="right")):
  jinkou[i] = element.text

print("沖縄県の推計人口")
print(f"総人口: {jinkou[0]}")
print(f"男: {jinkou[1]}")
print(f"女: {jinkou[2]}")
