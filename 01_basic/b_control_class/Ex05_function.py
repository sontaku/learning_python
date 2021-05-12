"""
    [ 함수 ]

     반복적인 구문을 만들어 함수로 선언하여 간단하게 호출만 하고자 한다

     def 함수명(매개변수):
        수행할 문장들
"""


# (1) 매개변수도 리턴값도 없는 함수
def func():
    print('inside func')
    # return 'Hello'


# 리턴값이 없어 None도 출력
print(func())


# (2) 리턴값이 있는 함수
def func(arg1, arg2):
    return arg1 + 100, arg2 + 10


result = func(1, 2)
print(result)

print('-------------------------')


# (2-2) 여러개의 리턴값이 있는 함수 -> 튜플로 하나의 리턴
def func(arg1, arg2):
    return arg1 + 100, arg2 + 10


res1, res2 = func(1, 2)
print(res1, res2)


# (3) 위치인자 (positional argument)
def func(greeting, name):
    print(greeting, '!!!!', name, '님')


func('안녕', '홍길동')
func('김길동', '잘가')

# (4) 키워드인자 (keyword argument)
func(name='김길동', greeting='잘가')


# (5) 함수 인자의 기본값
def func(greeting, name='홍길동'):
    print(greeting, '!!!!', name, '님')


func('헬로우', '존')
func('올라')

print('-----------------------------')


def func(a, b, c=100):
    return a * 2 + b * 3 + c * 4


print(func(c=1, b=2, a=3))
print(func(1, 2, 3))
print(func(1, 2))


# [참고] 알쓸신잡
def buggy(arg, result=[]):
    result.append(arg)
    print(result)


buggy('가')
buggy('나')
buggy('다', [1, 2, 3, 4])
buggy('라')

print('------------------------')
'''
#----------------------------------------------------------------
# (6) 위치 인자 모으기 (*)

첫번째와 두번째는 인자가 반드시 들어가고 세번째는 인자가 들어갈 수도 있고 없으면 0으로 초기화한다
그러나 네번째 인자부터는 정확히 모른다면?


'''


def func(a, b, c=0, *args):
    sum = a + b + c
    for i in args:
        sum += i
    return sum


print(func(4, 5))
print(func(4, 5, 6))
print(func(4, 5, 6, 7))
print(func(4, 5, 6, 7, 8, 9))  # args에 7,8,9가 튜플로 들어간다

print('----------------------------')
'''
#----------------------------------------------------------------
# (7) 키워드 인자 모으기
    - *args : 위치인자 모으기
    - **kwargs : 키워드인자 모으기

'''


def func(a, b, c=0, *args, **kwargs):
    sum = a + b + c
    for i in args:
        sum += i
    for k in kwargs:
        sum += kwargs[k]
    return sum


# print(func(4, 5))
# print(func(4, 5, 6))
# print(func(4, 5, 6, 7))
print(func(4, 5, kor=5, eng=10))
print(func(4, 5, 6, kor=5, eng=10))
print(func(4, 5, 6, 7, 8, 9, java=5, python=10))
