import requests
from bs4 import BeautifulSoup
import openpyxl


try:
    wb = openpyxl.load_workbook("navernews.xlsx")
    sheet = wb.active
#실패하면, 새로운 워크북을 만듭니다.
except:
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.append(["제목","언론사"])
    print("새로운 파일을 만들었습니다.")

keyword = input("검색어를 입력해주세요:")

for n in range(1, 100, 10):
    raw = requests.get("https://search.naver.com/search.naver?where=news&query="+keyword+"&start="+str(n),
                       headers = {"User-Agent":"Mozilla/5.0"})
    html = BeautifulSoup(raw.text,"html.parser")

    articles = html.select("ul.list_news li.bx")

    for ar in articles:
        title = ar.select_one("div.news_area>a").text
        source = ar.select_one("div.info_group>a.press").text
        print(title, source)

        sheet.append([title, source])


wb.save("navertv.xlsx")
