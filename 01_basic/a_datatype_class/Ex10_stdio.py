"""
    [ 콘솔 입력 처리 함수 ]
    - input() : 기본적으로 문자열로 입력받음
    - eval() : 함수로 감싸면 숫자 처리됨
    - int() / float() / str() 자료형변환  ( eval() 사용보다는 형변환을 권장 )
"""

name = input('이름을 입력하세요 : ')
print('당신의 이름은 %s입니다' % name)

# -------------------------------------------
# 나이를 입력받아 +1을 하여 출력하고 키를 실수형으로 입력받아 출력
age = input('나이를 입력하세요 : ')
print('나이 : %.1f' % float(age))

# ----------------------------------
# 단을 입력받아 구구단을 구하기
num = input('구구단을 외자~ 구구단을 외자~ 몇 단? : ')
for i in range(1, 10):  # 1 ~ 9
    # print(num, 'x', i, '=', i * int(num))
    print('{} * {} = {}'.format(num, i, int(num) * i))

# -----------------------------------------
# print() 함수
print('안녕' + '친구')
print('안녕' , '친구') # 띄어쓰기
print('안녕'  '친구')

for i in range(5):
    for j in range(5):
        print(i * j, end=', ' if j < 4 else "")
    print()

# -------------------------------------------------------
# 명령행 매개변수 받기 - java의 main() 함수의 인자
# [ 콘솔에서 자바를 실행 ] java Test abc def xxxx
# [ 콘솔에서 실행 ] python Ex10_stdio.py ourserver scott tiger
#                                   0      1      2      3
import sys
args = sys.argv[1:]
for i in args:
    print(i)