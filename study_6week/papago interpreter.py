#2022.03.04.pm.06.00

# Selenium을 사용해서 파파고(https://papago.naver.com)에서 "seize the day"라는 문장을 입력, 번역결과를 출력하는 프로그램을 만들어봅니다.
# 파파고 번역 서비스 이용 절차를 적어봅니다.
# 지연시간이 필요한 부분을 생각해봅니다.
# 코딩을 통해 번역결과를 출력합니다.
# *입력도구(input, textarea)를 찾아 .send_keys를 사용하세요.

from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")
driver.get("https://papago.naver.com/")
driver.implicitly_wait(1)

search_box = driver.find_element_by_css_selector("textarea#txtSource")
search_box.send_keys("seize the day")

button_box = driver.find_element_by_css_selector("button#btnTranslate")
button_box.click()

target = driver.find_element_by_css_selector("div#txtTarget span").text
print(target)