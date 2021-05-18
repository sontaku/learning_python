"""
네이버 로그인 페이지를 실행하기
    크롬에서 네이버 로그인 페이지를 개발자모드에서 확인하여
    로그인 폼의 아이디와 비밀번호 입력 name 확인
    아이디 : id
    비밀번호 : pw
"""
import time

from selenium import webdriver

# 0. 깃헙 로그인 정보
myID = 'jyson19@gmail.com'
myPW = 'del19831662'

# 1. webdriver 객체생성
driver = webdriver.Chrome('./webdriver/chromedriver.exe')
driver.implicitly_wait(3) # 3초 대기

# 2. 페이지 접근
driver.get('https://github.com/login')

driver.execute_script("document.getElementsByName('login')[0].value=\'" + myID + "\'")
driver.execute_script("document.getElementsByName('password')[0].value=\'" + myPW + "\'")
driver.find_element_by_name('commit').click()

# driver.get('https://github.com/sontaku?tab=repositories')
driver.find_elements_by_class_name('avatar-user')[1].click()
driver.find_elements_by_class_name('dropdown-item')[14].click()

# driver.close()