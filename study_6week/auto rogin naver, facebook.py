#2022.03.04.pm.04.54

from selenium import webdriver
import time

#네이버 로그인
driver = webdriver.Chrome("./chromedriver")
driver.get("https://nid.naver.com")

id_box = driver.find_element_by_css_selector("input#id")
pw_box = driver.find_element_by_css_selector("input#pw")

login_button = driver.find_element_by_css_selector("button.btn_login")

id_box.send_keys("kimhagam")
pw_box.send_keys("zxczxC.1")

login_button.click()

#페이스북 로그인
driver_other = webdriver.Chrome("./chromedriver")
driver_other.get("https://www.facebook.com/")

id_box_other = driver_other.find_element_by_css_selector("input#email")
pw_box_other = driver_other.find_element_by_css_selector("input#pass")

#css selector가 계속해서 변함
login_button_other = driver.find_element_by_css_selector("loginbutton")

id_box_other.send_keys("01035557903")
pw_box_other.send_keys("zxczxC.1")

login_button_other.click()

