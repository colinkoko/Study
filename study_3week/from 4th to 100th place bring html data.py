import requests
from bs4 import BeautifulSoup

raw = requests.get("https://tv.naver.com/r")
html = BeautifulSoup(raw.text,"html.parser")

clips = html.select("div.cds")

ranking = 4

for i in range(len(clips)):
    title = clips[i].select_one("dt.title")
    chn = clips[i].select_one("dd.chn")
    hit = clips[i].select_one("span.hit")
    like = clips[i].select_one("span.like")
    print(str(ranking)+"위 정보입니다.")
    print("title:",title.text.strip())
    print("channel name:",chn.text.strip())
    print("hit:",hit.text.strip()[4:])
    print("like:",like.text.strip()[5:])
    print()
    ranking = ranking + 1



