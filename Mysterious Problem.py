#2022.03.03.pm.06.10
#이 문제의 원본은 코알라 5주차 마지막 자율과제https://book.coalastudy.com/data_crawling/week5/ha1

# 다음영화 - 예매순위 페이지(http://ticket2.movie.daum.net/Movie/MovieRankList.aspx)에서 영화별 상세페이지에 접속하여 영화의 제목 / 평점 / 장르 / 감독 / 배우 데이터를 수집합니다.
# 예매순위 페이지에서 각 영화 상세페이지로 들어갈 수 있는 링크를 찾습니다.
# 상세페이지에서 원하는 데이터(제목, 평점, 장르, 감독, 배우)를 찾을 수 있는 선택자를 찾습니다.
# 코딩을 통해 데이터 수집기를 완성합니다.
# *hint) 다음영화 예매페이지의 경우, a태그에 저장되있는 링크는 완벽한 URL의 형태를 띄고 있습니다. 굳이 기존페이지의 주소를 붙여주지 않아도 상관없습니다 :)
# **hint) 영화의 상세페이지가 없는 경우에 에러가 발생할 수 있으니 확인하시고 코드를 완성해주시기 바랍니다.

#미완성인 이유: 위에 다음영화 예매순위 페이지 링크가 안 들어가져서
#최대한 비슷한 다음 영화 페이지에 들어가긴했지만 서로 다른 페이지니까 제대로 안 된거
#그리고 문제인게 select 선택자가 없다는거..
#또 다른 문제는 밑에 적어 놨듯이 도대체 왜 cast=html_each... 이거 왜 안 되는지 모르겠음

#내가 들어간 페이지는 https://movie.daum.net/ranking/reservation


import requests
from bs4 import BeautifulSoup

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

raw = requests.get("https://movie.daum.net/ranking/reservation",
                   headers={"User-Agent":"Mozilla/5.0"})
html = BeautifulSoup(raw.text, "html.parser")

movie = html.select("ol.list_movieranking li")

for mo in movie:
    title = mo.select_one("ol.list_movieranking li strong.tit_item a")

    url = "https://movie.daum.net/"+title.attrs["href"]
    raw_each = requests.get(url,headers={"User-Agent":"Mozilla/5.0"})
    html_each = BeautifulSoup(raw_each.text,"html.parser")
    info = html_each.select_one("div.info_detail")

    #데이터 찾고 수집
    title_each = info.select_one("h3.tit_movie span.txt_tit")

    #rating 선택자가 없음.. ==$0이라 requests, beautifulSoup만으로 안 되고
    #select함수로는 안 되니까 여러 다른 선택자중 xpath사용하는 selenium 공부 할 예정
    rating = info.select_one("dl.list_cont:nth-of-type(6)")
    genre = info.select_one("dl.list_cont:nth-of-type(2)")

    print("="*50)
    #여기서 rstrip()함수는 오른쪽 공백 제거 , 반대로 왼족은 lstrip()
    print(title_each.text.strip(),"\n",rating,"\n",genre.text.rstrip())

    # #감독인지 배우인지 구분
    # #나는 도대체 왜!!!!! cast이게 아무것도 선택을 안하는지 모르겠어
    # #선택 자체가 안 되니까 감독인지 배우인지 구분하는것도 안돼서 시간지체됨..
    # cast = html_each.select_one("ul.list_crewall li")
    # print(cast)
    # for ca in cast:
    #     print("@@@@@@@@@@@@")
    #     part = info.select_one("div.thumb_cont span")
    #     for pa in part:
    #         if "감독" in part.text:
    #             director = part.select_one("div.thumb_cont a")
    #             print(director.text)
    #             print("*****************정상작동******************")
    #             break



    print("="*50)

