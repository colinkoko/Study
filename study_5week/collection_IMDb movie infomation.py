#2022.03.02.am.08.12
# IMDb(https://www.imdb.com/movies-in-theaters/?ref_=nv_mv_inth)의
# 현재 상영중 영화목록에서 상영 중인 영화의 제목 /  감독 / 배우 데이터를 수집합니다.
# 컨테이너, 제목, 평점, 감독, 배우 데이터를 선택할 수 있는 선택자를 찾습니다.
# 파이썬을 통해 데이터를 수집할 수 있는 데이터 수집기를 만듭니다.
# (심화) 조건문을 활용하여 Action 장르의 영화만 출력합니다.

import requests
from bs4 import BeautifulSoup

raw = requests.get("https://www.imdb.com/movies-in-theaters/?ref_=nv_mv_inth")
html = BeautifulSoup(raw.text,"html.parser")

movies = html.select("div.list_item")

for mo in movies:
    title= mo.select_one("h4 a").text
    score = mo.select("span.metascore")


    info = mo.select("div.txt-block")
    directors = info[0].select("a")
    actors = info[1].select("a")
    genre = mo.select("p.cert-runtime-genre>span")

    ####
    genre_all = mo.select_one("p.cert-runtime-genre")
    if "Action" not in genre_all.text:
        continue
    ####

    print("="*50)
    print("-"*50)
    print("제목:")
    print(title)
    print("-" * 50)

    for g in genre:
        print(g.text)
    # for i in range(1,len(genre),2):
    #     genre1 = mo.select("p.cert-runtime-genre>span:nth-of-type("+str(i)+")")
    #     print(genre1.text)

    print("-"*50)
    print("평점:")
    for s in score:
        print(s.text)
    # print(score.text)

    print("-"*50)
    print("감독: ")
    for d in directors:
        print(d.text)
    print("-"*50)

    print("배우:")
    for a in actors:
        print(a.text)
    print("=" * 50)




