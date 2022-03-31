#2022.03.03 pm.01.16
# IMDb(https://www.imdb.com/movies-in-theaters/?ref_=nv_mv_inth)의
# 현재 상영중 영화목록에서 현재 상영중 영화의 상세페이지에 접속해 포스터를 저장합니다.
# 상세 페이지에 접속할 수 있는 링크주소를 수집합니다.
# 상세 페이지의 포스터를 선택할 수 있는 선택자를 찾습니다.
# 포스터 이미지가 저장되어 있는 속성을 찾아 포스터를 다운 받습니다.

import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

#url부르고 가공
raw = requests.get("https://www.imdb.com/movies-in-theaters/?ref_=nv_mv_inth",
                   headers={"Uesr-Agent":"Mozilla"})
html = BeautifulSoup(raw.text,"html.parser")

movie = html.select("div.sub-list>div.list_item")

for mo in movie:
    title = mo.select_one("td.overview-top>h4>a")
    url = "https://www.imdb.com/"+title.attrs["href"]

    raw_each = requests.get(url,headers={"Uesr-Agent":"Mozilla"})
    html_each = BeautifulSoup(raw_each.text,"html.parser")

    poster = html_each.select_one("div.Media__PosterContainer-sc-1x98dcb-1 div.ipc-poster div.ipc-media>img.ipc-image")
    poster_scr = poster.attrs["src"]

    urlretrieve(poster_scr,"poster/"+title.text+".png")