#2022.03.04.pm.02.43

# 구글지도(https://www.google.com/maps/)에 카페를 검색해서 검색된 카페들이 이름, 평점, 주소를 수집합니다.
# 구글지도에서 검색하고 결과를 확인하는 절차를 생각해봅니다.
# 컨테이너, 이름, 평점, 주소를 선택할 수 있는 선택자를 찾습니다.
# 코딩을 통해 데이터를 수집합니다.
# *구글의 경우 지연시간을 길게 주셔야 합니다. (평균 5 ~ 10초)

from selenium import webdriver
import time

driver = webdriver.Chrome("./chromedriver")
driver.get("https://www.google.com/maps/")
search_box = driver.find_element_by_css_selector("input#searchboxinput")
search_box.send_keys("카페")

button_box = driver.find_element_by_css_selector("button#searchbox-searchbutton")
button_box.click()

stores = driver.find_elements_by_css_selector("div.V0h1Ob-haAclf")

time.sleep(3)
while True:
    for store in stores:
        name = store.find_element_by_css_selector("div.V0h1Ob-haAclf a")
        addr = store.find_element_by_css_selector("")
        try:
            rating = store.find_element_by_css_selector("span.MW4etd")
        except:
            rating = "평점이 없습니다."

        try:
            addr = store.find_element_by_css_selector("")
        except:
            addr = "주소가 없습니다."

        print(name, rating, addr)
    try:
        next_button = driver.find_element_by_css_selector("button.hV1iCc.noprint")[1]
    except:
        print("데이터 수집 완료.")
        break
driver.close()












