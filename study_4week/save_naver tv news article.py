#2022.03.01.pm.11.00
#네이버 뉴스 1 ~10 페이지 각 제목과 언론사 출력하고 csv에 저장하기.

import requests
from bs4 import BeautifulSoup

f = open("naver articles.csv","w",encoding="UTF=8")
f.write("기사 제목,언론사\n")
for n in range(1,100,10):
    raw = requests.get("https://search.naver.com/search.naver?where=news&query=코알라&start="+str(n),
                       headers={'User-Agent':'mozilla/5.0'})
    html = BeautifulSoup(raw.text,"html.parser")

    articles = html.select("ul.list_news>li")

    for ar in articles:
        title = ar.select_one("div.news_area>a").text
        source = ar.select_one("div.info_group>a.press").text

        title = title.replace(",","")
        source = source.replace(",","")

        f.write(title+","+source+"\n")
f.close()
