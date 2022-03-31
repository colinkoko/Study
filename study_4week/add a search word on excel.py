#2022.03.01.pm.03.32

#엑셀에 검색어열 추가하기
# Stage4에서 완성한 네이버 뉴스기사 수집기를 통해 저장되는 엑셀양식에 "검색어"열을 추가합니다.
# 파일의 헤더위치에 "검색어" 카테고리를 추가합니다.
# "검색어" 카테고리에 입력한 키워드를 저장해줍니다.
# *Stage4에서 완성한 수집기 프로그램은 데이터가 누적되어 저장되므로 작동확인을 위해서 기존의 엑셀 파일을 삭제한 후 실행해주셔야합니다.

import requests
from bs4 import BeautifulSoup
import openpyxl

wb = openpyxl.Workbook()
sheet=wb.active
sheet.append(["검색어,", "기사제목", "언론사"])

keyword = input("검색어를 입력해 주세요:")
for i in range(1,100,10):
    raw = requests.get("https://search.naver.com/search.naver?where=news&query="+keyword+"&start="+str(i),
                       headers={"User-Agent":"Mozilla/5.0"})
    html = BeautifulSoup(raw.text, "html.parser")

    articles = html.select("ul.list_news li.bx")

    for ar in articles:
        title = ar.select_one("div.news_area>a.news_tit").text
        source = ar.select_one("div.info_group>a.press").text

        print(keyword, title, source)
        print()

        sheet.append([keyword, title, source])

wb.save("add a search word on excel.xlsx")
