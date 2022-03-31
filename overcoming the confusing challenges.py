#2022.03.02.am07.21

"""
*생각나는걸 다 글로 적어서 어순이 안 맞고 이상하며 이해하기 힘들다. 맨 밑에줄만 봐도된다.*
코알라 코딩공부 5주차를 하다 에러가 뜸. 계속 생각한 결과 에러가 뜬 이유를 정확히 파악했다.

"""
#우선 내가 코딩하려고 한것은 이것이다.

# import requests
# from bs4 import BeautifulSoup
#
# # 웹페이지에서 소스코드를 가져와 BeautifulSoup으로 파싱
# raw = requests.get("https://movie.naver.com/movie/running/current.nhn",
#                    headers={'User-Agent': 'Mozilla/5.0'})
# html = BeautifulSoup(raw.text, 'html.parser')
#
# # 컨테이너 수집하기
# movie = html.select("dl.lst_dsc")
# for m in movie:
#     # 영화별 데이터 수집하기
#     title = m.select_one("dt.tit a")
#     score = m.select_one("div.star_t1 span.num")
#
#     # nth-of-type을 활용해서 데이터를 선택합니다.
#     genre = m.select("dl.info_txt1 dd:nth-of-type(1) a")
#     directors = m.select("dl.info_txt1 dd:nth-of-type(2) a")
#     actors = m.select("dl.info_txt1 dd:nth-of-type(3) a")
#
#     # 구분선을 출력해줍니다.
#     print("=" * 50)
#     print("제목:", title.text)
#
#     print("-" * 50)
#     print("평점:", score.text)
#
#     # 장르, 감독, 배우는 데이터가 여러개일 수 있으므로
#     # 반복문을 통해 출력해줍니다.
#     print("-" * 50)
#     print("장르:")
#     for g in genre:
#         print(g.text)
#
#     print("-" * 50)
#     print("감독:")
#     for d in directors:
#         print(d.text)
#
#     print("-"*50)
#     print("배우:")
#     for a in actors:
#         print(a.text)

""" 
여기서 내가 잘못 쓴곳은 26, 27, 28번 줄이다. 여기서 select로 해야되는데 
select_one으로 한것이다. 그리고 _one을 잘 못쓴걸 확인하고 삭제했는데도 
에러가 뜬 것이다 그 이유는 뒤에 체이닝변수로 쓴 .text가 문제였던것이다. 

selec_one 뒤에만 .text로 할 수 있다.
"""
# 그리고 내가 지금 말할 이것때문에 이걸 쓰는 것이다.


# #2022.03.02.am04.29
#
# #불완전한 예제입니다.
# #( 개요, 감독, 출연이 모두 있어야 되는데 셋중 하나가 없는 경우가 있어 에러가 뜸)
#
# import requests
# from bs4 import BeautifulSoup
#
# raw = requests.get("https://movie.naver.com/movie/running/current.naver")
# html = BeautifulSoup(raw.text, "html.parser")
#
# movies = html.select("ul.lst_detail_t1>li")
#
# for mo in movies:
#     title= mo.select_one("dt.tit>a").text
#     rating = mo.select_one("div.star_t1>a>span.num").text
#
#
#     genre = mo.select_one("dl.info_txt1 dd:nth-of-type(1) a").text
#     directors = mo.select_one("dl.info_txt1 dd:nth-of-type(2) a").text
#     actor = mo.select_one("dl.info_txt1 dd:nth-of-type(3) a").text
#
#     print("="*50)
#     print("제목:",title)
#
#     print("-" * 50)
#     print("평점:", rating)
#
#     # 장르, 감독, 배우는 데이터가 여러개일 수 있으므로
#     # 반복문을 통해 출력해줍니다.
#     print("-" * 50)
#     print("장르:")
#     for g in genre:
#         print(g)
#
#     print("-" * 50)
#     print("감독:")
#     for d in directors:
#         print(d)
#     print("-"*50)
#     print("배우:")
#     for a in actor:
#         print(a)

"""

위 코드를 작성하면 에러가 뜬가. 그 에러들의 내용은 이러하다.
1.배우가 여럿있으면 다 떠야되지만 한명만 뜬다.
이유: 앞서 말했지만 82, 83, 84번 줄에 select_one 이어서 하나만 뜨는것이다.
    왜냐하면 select_one 자체가 하나만 저장하는것이고 뒤에 여러 인물을 생각해 반복문을 통한 
    print에서 여러 배우들을 반복해서 나오게하는 것인데, 하나만 저장한 것이라 하나만 나오는것임.
2.글자가 한줄에 한 글자씩 나옴.
이유:원래 하고자 한것이 select를 이용해 리스트 형식으로 저장하는 것이기에 
    ex) for a in actor:
        print(a)  
    여기서 리스트 하나에 한줄씩 나오게 하는건데 select_one으로 저장하였기에
    한 글자씩 나온것이다.
3.에러가 뜬 결정적 이유 
이유:위 코드를 돌리면 에러가 뜨는 곳은 84번째 줄이다. 
    나는 에러가 뜬이유가 위 주석에도 써놓았듯이 배우 정보가 없어서 그런것인줄알았다.
    여기서 배우정보란 지금 하는게 네이버에서 제공하는 개봉영화 정보를 출력하는것인데 
    모든 영화에 제목, 평점, 장르, 감독, 배우 이렇게 있어야 되는데 
    어떤 영화에 배우칸이 아예 없어 select도 없으니 에러뜨는건줄 알았는데 그건 아니다.
    
    정확한 이유는 뒤에 .text를 안 붙였더라면 에러가 안 뜰것이다.
    없는것을 select하면 아무것도 없는것을 선택해서 에러가 안뜨지만
    없는것을 text로 변환한다고 하는 체이닝변수에서 에러가 뜬것이다.

"""

#한다디로
"""
뭔가 말도 잘 못쓰고 이해 못하게 써놨는데 간단하게 써보자면 

네이버 개봉영화 데이터를 출력하는걸 코딩하려고 했는데 
에러가 뜬것이다. 개봉영화 데이터에서 배우가 없어 에러가 뜬줄만 알았는데 
에러가 뜬 이유는 배우가 없는것을 select해서가 아닌, 체이닝변수로 쓴 .text에서 뜬것이다.

해결법은 select_one이 아닌 select로 쓰고 뒤에 .text는 쓰면안된다.
그럼 언제 text를 쓰냐? 그건 뒤에 print할때 뒤에 .text를 쓰면 해결이 된다. 
    
"""

"""
#2022.03.02.am.08.55
********개정본********

방금하면서 확실히 알았는데 선택하는데 선택할게 없을떄는 에러가 안뜨지만 
그걸 .text로 할때 에러가 뜸 그래서 전에는 print할떄 .text로 붙이면 에러가 
안 뜰거라 했는데 그것도 에러가 뜸 (아까 쓰면서도 살짝 헷갈리긴했음)
그러니까 for을 이용해야됨. 지금도 정확히는 모르지만 내 생각에는 
for변수가 반복하는건데 없으니까 반복자체를 안하면서 에러가 안뜨는걸거야.
코알라에서도 이렇게 표현하니까 이렇게 표현하도록! 
ex) for a in actor:
        print(a.text)
"""