#2022.03.01.am5.10

#Y-Combinator 스타드업 뉴스기사 1~3페이지까지 순위, 제목을 수집
import requests
from bs4 import BeautifulSoup

for n in range(1,4):
    raw = requests.get("https://news.ycombinator.com/news?p="+str(n))
                # 안티 크롤링이 있을 수 있어 headers={"Uesr-Agent":"Mozilla/5.0"}를 붙여주면 해결 됨

    html = BeautifulSoup(raw.text, "html.parser")
    articles = html.select("tr.athing")

    for ar in articles:
        rank = ar.select_one("span.rank").text
        title = ar.select_one("tr.athing>td.title>a").text
        #source = ar.select_one("span.sitebit.comhead").text
        #출처도 쓰고싶은데 출처가 없는 뉴스가 있어 에러가 뜸
        #그래서 출처없는 뉴스는 건너띄고 있는 뉴스만 뜨게 하고 싶음.
        print(rank,title)
        print()
