# ------------------------------------------------------
"""
   (2) for문
        for <타켓변수> in 집합객체 :
            문장들
        else:
            문장들

        ` 반복문 뒤에 else는 반복하는 조건에 만족하지않으면 실행

   (3) while 문
        while 조건문 :
            문장들
        else :
            문장들

"""
a = 112  # 숫자형
b = ['1', '2', '3']  # 리스트
c = '987'  # 문자열
d = tuple(b)  # 튜플
e = dict(k=5, j=6)  # 딕셔너리

# for entry in a: # a는 반복이 안되지만 b부터 e까지는 반복된다.
#    print(entry)

for entry in e.items():
    print(entry)
    print('key :', entry[0], ', value :', entry[1])

print('---------------------')

for k, val in e.items():
    print('key :', k, ', value:', val)

# 1~10 까지의 합
sum = 0
for i in range(1, 11):
    sum += i
print('sum=', sum)

# 1~10 까지의 홀수의 합
sum = 0
for i in range(1, 11, 2):
    sum += i
print('sum=', sum)

# =========================================================
# while  ( 안해도 될듯 )

# a = 1
# while True:  # 무한루프
#    if a == 1:
#        print(a)
#        break

a = ['a', 'b', 'c']
while a:  # 조건
    data = a.pop()
    print(data)
else:  # for문이나 와일문 조건문에 위배됐을때
    print('끝')

print('------------------------')
"""
[과제] 2단부터 9단까지 이중 반복문으로 출력
"""
for i in range(2, 10):  # 2 ~ 9
    print('-- {}단 시작 --'.format(i))
    for j in range(1, 10):  # 1 ~ 9
        print('  {} X {} = {}'.format(i, j, i * j))
    print('--------------')

list_data_a = [1, 2]
list_data_b = [3, 4]
for i in list_data_a:
    for j in list_data_b:
         result = i + j
print(result) # 4 5 5 6
