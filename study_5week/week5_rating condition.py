#2022.03.02.am.07.55

import requests
from bs4 import BeautifulSoup

# 웹페이지에서 소스코드를 가져와 BeautifulSoup으로 파싱
raw = requests.get("https://movie.naver.com/movie/running/current.nhn",
                   headers={'User-Agent': 'Mozilla/5.0'})
html = BeautifulSoup(raw.text, 'html.parser')

# 컨테이너 수집하기
movie = html.select("dl.lst_dsc")
for m in movie:
    # 영화별 데이터 수집하기
    title = m.select_one("dt.tit a")
    score = m.select_one("div.star_t1 span.num")

    # nth-of-type을 활용해서 데이터를 선택합니다.
    genre = m.select("dl.info_txt1 dd:nth-of-type(1) a")
    directors = m.select("dl.info_txt1 dd:nth-of-type(2) a")
    actors = m.select("dl.info_txt1 dd:nth-of-type(3) a")

    #####################################
    #추가

    #genre_all을 수집
    #"액션"장르가 아니면 continue
    genre_all = m.select("dl.info_txt1 dd:nth-of-type(1) span.link_txt")
    if "액션" not in genre_all.text:
        continue
    ####################################

    # 구분선을 출력해줍니다.
    print("=" * 50)
    print("제목:", title.text)

    print("-" * 50)
    print("평점:", score)

    # 장르, 감독, 배우는 데이터가 여러개일 수 있으므로
    # 반복문을 통해 출력해줍니다.
    print("-" * 50)
    print("장르:")
    for g in genre:
        print(g.text)

    print("-" * 50)
    print("감독:")
    for d in directors:
        print(d.text)

    print("-" * 50)
    print("배우:")
    for a in actors:
        print(a.text)

    print("="*50)

