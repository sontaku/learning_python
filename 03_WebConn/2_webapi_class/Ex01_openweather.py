"""
    전세계날씨제공 API : http://openweathermap.org

    1. 회원가입 : 메뉴 > Sign Up > 사용용도 : Education > 대충가입 (무료는 1번에 60번 호출 가능 )
    2. 개발자모드 : Sign In > API Keys 에서 내가 발급받은 키 (추가 키 가능)
    3. 발급받고 바로 지정 안됨 (시간소요)
"""

# API 키를 지정합니다. 자신의 키로 변경해서 사용해주세요.
import json

apikey = "1db47184ebbc18af53fd996be840d270"

# 날씨를 확인할 도시 지정하기
cities = ["Seoul,KR", "Tokyo,JP", "New York,US"]

# url 지정
api = "http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}"

# 켈빈 온도를 섭씨 온도로 변환하는 함수
k2c = lambda k: k - 273.15

import requests
for cname in cities:
    url = api.format(city=cname, key=apikey)
    res = requests.get(url)
    # print(res.text)
    # print(type(res.text)) # str
    data = json.loads(res.text)

    # 결과 처리
    print('======= 도시 : ', data["name"] + ' =======')
    print('날씨 : ', data["weather"][0]["main"])
    print('온도 : ', k2c(data["main"]['temp']))

    # 최저온도, 최고온도, 기압, 풍속
    print('최저온도 : ', k2c(data["main"]['temp_min']))
    print('최고온도 : ', k2c(data["main"]['temp_max']))
    print('기압 : ', data["main"]['pressure'])
    print('풍속 : ', data["wind"]['speed'])


