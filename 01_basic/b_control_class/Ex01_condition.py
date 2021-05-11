"""
 [ 제어문 ]
    - 파이썬은 들여쓰기를 하여 블록{}을 대신 표현한다
    - 들여쓰기는 탭과 공백을 섞어 쓰지 말자

    [ex]
    if a>b:
        print(a)
            print(b)  => 에러발생

    (1) if 문
        if 조건식A :
            문장들
        elif 조건식B :
            문장들
        else :
            문장들

        ` 조건식이나 else 뒤에는 콜론(:) 표시
        ` 조건식을 ( ) 괄호 필요없다
        ` 실행할 코드가 없으면 pass
        ` 파이썬은 switch 문 없음
"""

# 거짓(False)의 값
i = 0;
i2 = 0.0
i3 = ""
i4 = str()
i5 = list()
i6 = tuple()
i7 = set()
i8 = dict()
i9 = {}
i10 = None

print(type(i9))

a = 0
if a:
    print('True1')
else:
    print('False1')

# (2) 논리연산자 이용한 조건
a = 10 # True
b = -1 # True
if a and b:
    print('True2')
else:
    print('False2')

if a or b:
    print('True3')
else:
    print('False3')

# [참고] 자바의 short circuit logic
print(a and b)
print(a or b)


# (3) 블록에 대한 정리
a = 10
if a:
    print('A')
    print('B')
    print('C')

a = 10
if a:
    print('A')
print('B')
    #print('C')

print('-----------------------')

a = 10
if not a:
    c = 10
elif not b:
    c = 20
else:
    c = 30
print(c)

print('--------------')

# (4)
word = 'korea'
print(word.find('k')) # 찾아서 0 -> False
if word.find('k'):
    print('1>' + word)

print(word.find('z')) # 못찾아서 -1 -> 있는값이라고 판단해 True
if word.find('z'):
    print('2>' + word)