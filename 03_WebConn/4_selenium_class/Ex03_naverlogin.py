"""
네이버 로그인 페이지를 실행하기
    크롬에서 네이버 로그인 페이지를 개발자모드에서 확인하여
    로그인 폼의 아이디와 비밀번호 입력 name 확인
    아이디 : id
    비밀번호 : pw
"""
import time

from selenium import webdriver

# 0. 네이버 로그인 정보
myID = '아이디'
myPW = '패스워드'

# 1. webdriver 객체생성
driver = webdriver.Chrome('./webdriver/chromedriver.exe')
driver.implicitly_wait(3) # 3초 대기

# 2. 페이지 접근
driver.get('https://nid.naver.com/nidlogin.login')

# 네이버의 경우 아래 방식이 막혀있음
# driver.find_element_by_name('id').send_keys(myID)
# driver.find_element_by_name('pw').send_keys(myPW)
# driver.find_element_by_name('log.login').click()

# 자바스크립트를 통해 전송
# 이거도 막힘..
driver.execute_script("document.getElementsByName('id')[0].value=\'" + myID + "\'")
driver.execute_script("document.getElementsByName('pw')[0].value=\'" + myPW + "\'")
driver.find_element_by_id('log.login').click()