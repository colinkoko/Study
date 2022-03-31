#2022.03.05.pm.07.13
#
# 인스타그램에서 ootd 해시태그 검색결과(https://www.instagram.com/explore/tags/ootd/) 페이지에 접속해서 12개 포스트의 본문 내용을 수집합니다.
# 본문 데이터 수집을 수집을 위한 절차를 생각해봅니다.
# 선택자와 지연시기를 생각해봅니다.
# 코딩을 통해 본문 수집기를 완성합니다.
# *인스타그램의 class/id는 자동 생성프로그램에 의해 랜덤하게 생성됩니다.

#미완성 현재시간 pm.10.35 ..오래걸림 여러가지 장애물들이 많았음
#코알라에서는 자동으로 로그인이 되어있는데 나는 따로 로그인을 해야되는걸 만들어야됐으며,
#로그인 버튼이 눌리지가않음 (눌리는데 두번째 선택자가 눌림)


#
# from selenium import webdriver
#
#
#
# driver = webdriver.Chrome("./chromedriver")
# driver.implicitly_wait(4)
# driver.get("https://www.instagram.com/explore/tags/ootd/")
# id_box = driver.find_elements_by_css_selector("input._2hvTZ")[0]
# pw_box = driver.find_elements_by_css_selector("input._2hvTZ")[1]
# login_box = driver.find_elements_by_css_selector("div.DhRcB button.sqdOP")[0]
#
# id_box.send_keys("01035557903")
# pw_box.send_keys("zxczxccxzcxz.1")
# login_box.click()
#
# #로그인 정보저장 나중에하기
# later = driver.find_elements_by_css_selector("button.sqdOP")[2].click()
#
# elements = driver.find_elements_by_css_selector("div.v1Nh3")
#
# for e in elements:
#     internal = e.find_element_by_xpath("//div/a")
#     internal.click()
#     print("성공")
#     break



#정답


from selenium import webdriver
import time

# 크롬창(웹드라이버) 열기
driver = webdriver.Chrome("./chromedriver")

# ootd 태그 검색결과 페이지 접속
driver.get("https://www.instagram.com/explore/tags/ootd/")

# (선택)로그인 안내 창 닫기
login_close = driver.find_element_by_css_selector("button.dCJp8")
login_close.click()

# 컨테이너(포스트) 12개 저장
instagram = driver.find_elements_by_css_selector("div.v1Nh3")
instagram = instagram[:12]

# 컨테이너 반복하기
for insta in instagram:
    # 포스트 클릭하기
    insta.click()

    # 시간 지연
    time.sleep(1)

    # 본문 선택 후 출력
    post = driver.find_element_by_css_selector("div.C4VMK span").text
    print(post)

    # 닫기 버튼 클릭
    but_close = driver.find_element_by_css_selector("button.ckWGn")
    but_close.click()