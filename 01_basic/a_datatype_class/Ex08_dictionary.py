"""
    [ dictionary 형 ]

    1- 키와 값으로 구성 ( 자바의 map 와 유사 )
    2- 저장된 자료의 순서는 의미 없음
    3- 중괄호 {} 사용
    4- 변경가능

    ` 사전.keys() : key만 추출 (임의의 순서)
    ` 사전.values() : value만 추출 (임의의 순서)
    ` 사전.items() : key와 value를 튜플로 추출 (임의의 순서)
"""

print('--------- 1. 딕셔너리 요소 --------------- ')
dt = {1:'one', 2:'two', '3':'three', 1:'하나', 3:'셋'}
print(dt)
# 키값이 1인 요소 출력
print(dt[1])
# 키값이 3인 요소 출력 => 존재하지않음
# print(dt[3])
# 키값이 '3'인 요소 출력
print(dt['3'])


# 키는 숫자와 문자 그리고 튜플이여야 한다. 즉 리스트는 안된다.
# 리스트의  값이 변경 가능하다. 그러나 키값을 변경하면 안되므로 리스트는 안된다
dt2 = {1:'one', 2:'two', (3, 4):'turple'}
print(dt2[3,4])

print('--------- 2. 딕셔너리 추가 및 수정  --------------- ')
# 딕셔너리에 값 추가 및 수정
dt['korea'] = 'seoul'
print(dt)

dt['korea'] = '서울'
print(dt)

# 여러개 추가할 때
dt.update({5:'kim', 6:'hong', 7:'kang'})
print(dt)

print('--------- 3. Key로 Value값 찾기  --------------- ')
print(dt.get(9, '없음')) # 존재하지 않으면 None


# Key와 Value만 따로 검색
print(dt.keys())
print(dt.values())
print(dt.items())