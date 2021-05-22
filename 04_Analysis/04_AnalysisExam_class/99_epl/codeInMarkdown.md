### 링크 접속

```python
# selenium으로 URL에 접속
from selenium import webdriver
import time
# webdriver 설치 경로 확인
driver = webdriver.Chrome('C:/Users/jyson/git/learning_python/03_WebConn/4_selenium_class/webdriver/chromedriver.exe')

# 최대사이즈
driver.maximize_window()

url = "https://www.premierleague.com/tables"
driver.get(url)
```



### 쿠키 제거

```python
driver.implicitly_wait(3)
driver.find_element_by_class_name('cookies-notice-accept').click()
driver.find_element_by_id('advertClose').click()
```



### 라운드별 데이터 크롤링

```python
# 리스트 갯수
ul = driver.find_elements_by_xpath('/html/body/main/div[2]/div[1]/div[1]/section/div[3]/ul/li')
print(len(ul))

round = [] # 라운드
rank = [] # 순위

# 라운드 순회
for i in range(len(ul) - 1):
    time.sleep(1)
    driver.find_elements_by_class_name('current')[2].click()
    time.sleep(1)
    ul[i + 1].click()
    time.sleep(1)
    tr = driver.find_element_by_xpath("//tr[@data-filtered-table-row-name='Tottenham Hotspur']")

    print('라운드 : ' + str(i + 1) + ', 순위 : ' + str(tr.text.split("\n")[0]))
    round.append(i + 1)
    
    # 데이터 크롤링 실패시
    if tr.text.split("\n")[0] == '':
        while(tr.text.split("\n")[0] == ''):
            print("재시도 . . .")
            driver.refresh()
            time.sleep(3)
            driver.get(url)

            time.sleep(1)
            driver.find_elements_by_class_name('current')[2].click()
            time.sleep(1)
            ul = driver.find_elements_by_xpath('/html/body/main/div[2]/div[1]/div[1]/section/div[3]/ul/li')
            ul[i + 1].click()
            time.sleep(5)
            tr = driver.find_element_by_xpath("//tr[@data-filtered-table-row-name='Tottenham Hotspur']")

            print('라운드 : ' + str(i + 1) + ', 순위 : ' + str(tr.text.split("\n")[0]))

            rank.append(int(tr.text.split("\n")[0].strip()))
        else:
            print('라운드 : ' + str(i + 1) + ', 순위 : ' + str(tr.text.split("\n")[0]))
    else:
        rank.append(int(tr.text.split("\n")[0].strip()))
```



### 데이터 시각화

```python
from matplotlib import pyplot as plt
import matplotlib.ticker as mticker

plt.figure(figsize=(20, 8))
# X축 눈금
plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38])
plt.ylim([int(20), int(0)]) # Y축의 범위

plt.title('THS rankchart')
plt.gca().title.set_size(25)

plt.gca().yaxis.set_major_formatter(mticker.FormatStrFormatter('%i')) # 소수점 제거

# 격자무늬
plt.grid(True, axis='y')

plt.plot(round, rank, color='blue',  marker='o', label=('THS'))
plt.legend(loc=4)
plt.show()
```

