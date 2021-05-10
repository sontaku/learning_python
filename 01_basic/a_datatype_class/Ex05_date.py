import datetime
today = datetime.date.today();
print('today is ', today)

from datetime import date, timedelta
today = date.today()
print('today is ', today)

# 년도, 월, 일 출력
print('연도: ', today.year)
print('월: ', today.month)
print('일: ', today.day)

# 날짜 계산
today = date.today()
print('어제: ', today + timedelta(days=-1))

# 일주일전
print('일주일전: ', today + timedelta(days=7))

# 열흘 후
print('열흘 후: ', today + timedelta(days=10))


# 날짜 변환 (중요)
# 1) date to string : strftime()
from datetime import datetime
today = datetime.today()
print(today.strftime('%Y-%m-%d %H:%M'))

# 2) string to date : strptime()
from datetime import datetime
strToday = '2021-05-10 10:30:30'
print(datetime.strptime(strToday, '%Y-%m-%d %H:%M:%S'))
