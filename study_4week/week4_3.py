import requests
from bs4 import BeautifulSoup

f = open("navertv.csv","w",encoding="UTF-8")

f.write("제목,채널명,재생 수,좋아요 수\n")

raw = requests.get("https://tv.naver.com/r")
html = BeautifulSoup(raw.text, "html.parser")

# 1위 - 100위 컨테이너 선택자: dl.cds_info
clips = html.select("dl.cds_info")

for cl in clips:
    # 수정된 부분
    title = cl.select_one("dt.title").text.strip()
    chn = cl.select_one("dd.chn").text.strip()
    hit = cl.select_one("span.hit").text.strip()
    like = cl.select_one("span.like").text.strip()

    title = title.replace(",","")
    chn = chn.replace(",","")
    hit = hit.replace(",","")
    like = like.replace(",","")

    hit = hit.replace("재생 수","")
    like = like[5:]


    print("제목", title)
    print("채널명", chn)
    print(hit)
    print(like)
    print("="*50)



    f.write(title+","+chn+","+hit +","+like+"\n")

f.close()