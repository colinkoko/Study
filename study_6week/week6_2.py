# # 2022.03.04.pm.01.08
#
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# driver = webdriver.Chrome("./chromedriver")
#
# driver.get("https://map.naver.com")
# driver.implicitly_wait(2)
# search_box = driver.find_element_by_css_selector("input.input_search")
# search_box.send_keys("식당")
# search_box.send_keys(Keys.ENTER)
#
# # driver.implicitly_wait(1)
#
# # driver.implicitly_wait(5)
#
# for n in range(1,3):
#     stores = driver.find_elements_by_css_selector("div._3hn9q")
#     for store in stores:
#         name = store.find_element_by_css_selector("span.OXiLu").text
#         # addr = store.find_element_by_css_selectoer("a span._2yqUQ").text
#         # phone = store.fine_element_by_css_selector("span._3ZA0S").text
#
#         print(name)
#     # page_bar = driver.find_elements_by_css_selector("div._2ky45>*")
#     #
#     # page_bar[n+1].click()


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome("./chromedriver")
driver.get("https://map.naver.com")
driver.implicitly_wait(5)
search_box = driver.find_element_by_css_selector("input#input_search1646452908090")

search_box.send_keys("식당")
search_box.send_keys(Keys.ENTER)

for i in range(1,20):
    stores = driver.find_elements_by_css_selector("ul li._1EKsQ")
    for store in stores:
        name = store.find_elements_by_css_selector("span.OXiLu")

        try:
            tel = store.find_element_by_css_selector("value").text
        except:
            tel ="전화번호 없음"
        print(name.text)
        print(tel)

    page_bar = driver.find_elements_by_css_selector("value")
    try:
        if n%5 != 0:
            page_bar[i%5+1].click()
        else:
            page_bar[6].click()
    except:
        print("데이터 수집 완료")
        break
















