# [추가] 함수도 객체이다
def case1():
    print('case-1')


def case2():
    print('case-2')


def case3():
    print('case-3')


f = {'a1': case1, 'a2': case2, 'a3': case3}
print(f['a1'])
f['a1']()

# ---------------------------------------
# 글로벌 변수와 지역변수
print('------------------------')
temp = '글로벌 변수'


def func():
    # print('0>', temp)
    global temp
    temp = '지역 변수'
    print('1>', temp)


func()
print('2>', temp)

'''
#----------------------------------------------
# 람다함수 - 한번 사용하고 버리는 함수
# 파이션에서는 람다함수를 한 줄로 작성???

    파이썬 3.x부터는 람다를 권장하지 않는다고.
    몇몇 개발자들이 람다함수 사용시 직관적이지 않다는 이유라는데
    
    종종 사용됨
'''
print('----------------------')


def f(a, b):
    return print(a + b)


f(3, 2)

f = lambda a, b: print(a + b)
f(3, 2)

# -----------------------------------------------------------
"""  맵리듀스
    (1) map()
         ` 연속 데이터를 저장하는 시퀀스 자료형에서 요소마다 같은 기능을 적용할 때 사용
         ` 형식 : map(함수명, 리스트형식의 입력값)
         ` 파이썬 3.x에서는 list(map(calc, ex)) 반드시 list를 붙여야 리스트 형식으로 반환된다
           파이썬 2.x에서는 list 없이도 리스트 형식으로 반환
    (2) reduce()
         ` 리스트 같은 시퀀스 자료형에 차례대로 함수를 적용하여 모든 값을 통합하는 함수    
    
    파이썬 2.x에서는 많이 사용하던 함수이지만, 최근 문법의 복잡성으로 권장하지 않는 추세란다.
"""
print('---------------')


def cals(x):
    print('연산 전 : ', x)
    return x * 2


data = [1, 2, 3, 4, 5]
# 내부적으로 반복문을 사용한다고 상상
print(list(map(cals, data)))

print('-----------------')

# reduce
from functools import reduce
data = [1, 2, 3, 4, 5]
def f(a, b):
    return a + b
print(reduce(f, data))



print('-------------')
def factorial_calculator(n):
    if n in (0, 1):
        return 1
    else:
        return n * factorial_calculator(n - 1)

# if n > 1:
#  n * n-1
#  n = n - 1
#  factorial_calculator(n)
print(factorial_calculator(5))