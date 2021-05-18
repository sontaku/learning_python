'''
1. 크롬웹드라이버로 구글 사이트 열기

2. 실제 크롬창에서 '파이썬'라고 검색버튼을 누른다.
    개발자모드(F12)에서 이 부분을 보면
    <input name='q' value='파이썬'~~ >
    그리고 'google검색' 버튼이 type='submit' 인거 확인
'''

# [1]
from selenium import webdriver

# 1. webdriver 객체생성
driver = webdriver.Chrome('./webdriver/chromedriver.exe')
driver.implicitly_wait(3) # 3초 대기

# 2. 페이지 접근
driver.get('http://www.google.com')

#----------------------------------------------
# [2]
# 구글 검색창 input name : q
search = driver.find_element_by_name('q')
search.send_keys('코로나 극복')
# 폼 태그 안에 인풋 타입이 텍스트인 애가 하나만 있으면 엔터 쳤을 때 자동 서브밋
search.submit()

driver.close()