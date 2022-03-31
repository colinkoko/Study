#2022.03.01.am5.58

# 네이버뉴스 기사 데이터 수집과 같은 방법으로 다음뉴스 기사 데이터를 1-3페이지까지 수집하는 수집기를 만들어봅니다.
# 수집목표: 기사제목/기사 요약
# 컨테이너, 기사제목, 기사 요약 선택자 찾기
# 페이지를 변환하는 요청값 규칙 찾기
# *참고: 다음 뉴스페이지는 역으로 headers가 있는 데이터 요청을 크롤링 시도라고 이해합니다. 이번에는 헤더값을 넣지 않고 수집기를 만들어봅니다.
# 코딩을 통해 데이터 수집기 만들기

import requests
from bs4 import BeautifulSoup

for n in range(1,4):
    raw = requests.get("https://search.daum.net/search?w=news&DA=PGD&enc=utf8&cluster=y&cluster_page=1&q=%EC%BD%94%EC%95%8C%EB%9D%BC&p="+str(n))
    html = BeautifulSoup(raw.text,"html.parser")

    articles = html.select("ul.list_news>li")

    for ar in articles:
        title = ar.select_one("div.wrap_cont>a").text
        summary = ar.select_one("div.wrap_cont>p.desc").text

        print(title, summary)
        print()

