#2022.03.02.am.03.29

# 네이버 시리즈 e북 인기 TOP100 페이지에서(https://series.naver.com/ebook/top100List.nhn)
# 제목/저자 데이터를 수집하여 원하는 방식으로 저장합니다. (csv, xlsx)

import requests
from bs4 import BeautifulSoup
import openpyxl

try:
    wb = openpyxl.load_workbook("ddd")

    print("파일을 로드합니다")

except:
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.append(["제목", "저자"])

    print("새로운 파일을 만듭니다.")

    for n in range(1,6):
        raw = requests.get("https://series.naver.com/ebook/top100List.series?page="+str(n),
                           headers={"Uesr-Agent":"Mozilla/5.0"})
        html = BeautifulSoup(raw.text,"html.parser")

        books = html.select("ul.v1>li")

        for bo in books:
            title=bo.select_one("ul.v1>li>a>strong").text
            writer=bo.select_one("ul.v1>li>a>span.writer").text

            print(title, writer)

            sheet.append([title, writer])

wb.save("save_naver e-book data.xlsx")



