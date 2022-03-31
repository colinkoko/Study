import requests
from bs4 import BeautifulSoup

# 반복 1: 기사번호를 변경시키면서 데이터 수집을 반복하기
# 1 ~ 100까지 10단위로 반복
for n in range(1,100,10):
    raw = requests.get("https://search.naver.com/search.naver?where=news&query=코알라&start="+str(n),
                       headers={'User=Agent':'Mozilla/5.0'})
    html = BeautifulSoup(raw.text,"html.parser")
    articles = html.select("ul.list_news>li")

    for i in range(0,10):
        title = articles[i].select_one("div.news_area>a").text
        source = articles[i].select_one("a.info.press").text

        print(title,"*"*5,source)
        print()



