import requests
from bs4 import BeautifulSoup

raw = requests.get("https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%BD%94%EC%95%8C%EB%9D%BC")
html = BeautifulSoup(raw.text,"html.parser")

articles = html.select("ul.list_news>li")

#첫번째 기사에 대한 제목/언론사를 수집해서 반복 출력

#for i in range() 방법

for i in range(0,10):
    title = articles[i].select_one("div.news_area>a").text
    source = articles[i].select_one("a.press").text
    print("기사제목: "+title)
    print("언론사: "+source)
    print()
#for ar in articles 방법

# for ar in articles:
#     title = ar.select_one("div.news_area>a").text
#     source = ar.select_one("a.press").text
#
#     print(title,source)





