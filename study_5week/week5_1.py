#2022.03.02.am04.29

#불완전한 예제입니다.
#( 개요, 감독, 출연이 모두 있어야 되는데 셋중 하나가 없는 경우가 있어 에러가 뜸)
#출연이 없어사 에러가 뜬게 아님, 이유와 해결법은 overcoming the confusing challenges에 적음

import requests
from bs4 import BeautifulSoup

raw = requests.get("https://movie.naver.com/movie/running/current.naver")
html = BeautifulSoup(raw.text, "html.parser")

movies = html.select("ul.lst_detail_t1>li")

for mo in movies:
    title= mo.select_one("dt.tit>a").text
    rating = mo.select_one("div.star_t1>a>span.num").text


    genre = mo.select_one("dl.info_txt1 dd:nth-of-type(1) a").text
    directors = mo.select_one("dl.info_txt1 dd:nth-of-type(2) a").text
    actor = mo.select_one("dl.info_txt1 dd:nth-of-type(3) a").text

    print("="*50)
    print("제목:",title)

    print("-" * 50)
    print("평점:", rating)

    # 장르, 감독, 배우는 데이터가 여러개일 수 있으므로
    # 반복문을 통해 출력해줍니다.
    print("-" * 50)
    print("장르:")
    for g in genre:
        print(g)

    print("-" * 50)
    print("감독:")
    for d in directors:
        print(d)
    print("-"*50)
    print("배우:")
    for a in actor:
        print(a)