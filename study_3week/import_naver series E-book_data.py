#2022.03.01.am5.40

# 네이버 시리즈 e북 인기 TOP100 페이지에서(https://series.naver.com/ebook/top100List.nhn) 아래 데이터를 수집하는 코드를 만들어봅니다.
# 컨테이너, 제목, 저자를 선택하는 선택자를 찾아냅니다.
# 파이썬을 활용해서 데이터 수집기를 만들어냅니다.
# (심화)1-20위, 21-40위, ... , 81-100위 서적을 모두 수집할 수 있는 요청값을 찾아 수집기를 만들어 냅니다.

import requests
from bs4 import BeautifulSoup

for n in range(1,6):
    raw = requests.get("https://series.naver.com/ebook/top100List.series?page="+str(n))
    html = BeautifulSoup(raw.text,"html.parser")

    container = html.select("div#content li")

    for co in container:
        title = co.select_one("div#content li>a strong").text
        writer = co.select_one("span.writer").text

        print(title,writer)
        print()


