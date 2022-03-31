#2022.03.02.am.03.57

#다음뉴스 기사 데이터(기사제목/기사요약)를
# 1-3페이지까지 수집하여 원하는 방식으로 저장합니다. (csv, xlsx)

import requests
from bs4 import BeautifulSoup


f = open("save daum news.csv", "w")

f.write("검색어,기사 제목,기사요약\n")

keyword = input("검색할 내용을 입력해주세요:")
for i in range(1,11):
    raw = requests.get("https://search.daum.net/search?w=news&q="+keyword+"&p="+str(i))
    html = BeautifulSoup(raw.text,"html.parser")

    articles = html.select("ul.list_news>li")

    for ar in articles:
        title = ar.select_one("a.tit_main.fn_tit_u").text
        summary = ar.select_one("p.desc").text

        title = title.replace(",","")
        summary = summary.replace(",","")


        print(keyword+"#"*10+title+"\n"+summary)
        print()

        f.write(keyword+","+title+","+summary+"\n")

f.close()

