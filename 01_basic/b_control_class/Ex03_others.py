msg = '행복해'  # 문자열
li = ['a', 'b', 'c']  # 리스트
tpl = ('ㄱ', 'ㄴ', 'ㄷ')  # 튜플
di = {'k': 5, 'j': 6, 'l': 7}  # 딕셔너리

# (1) unpacking : 요소분할
c1, c2, c3 = di
print(c1, di[c1])
print(c2, di[c2])
print(c3, di[c3])

alist = [(1, 2), (3, 4), (5, 6)]
'''
    [출력결과]
    1 + 2 = 3
    3 + 4 = 7
    5 + 6 = 11
'''
for i, j in alist:
    print('{} + {} = {}'.format(i, j, i + j))

print('----------------------')

# (2) enumerate()
#   java의 iterator의 옛날 이름(비슷)
user_list = ['개발자', '코더', '프로그래머']
for val in user_list:
    print(val)

print('------------')
for val in enumerate(user_list):
    print(val)

print('------------')
for idx, val in enumerate(user_list):
    print(idx, '>', val)

print('-------------------')
# (3) zip() : 중요함
days = ['월', '화', '수']
doit = ['잠자기', '밥먹기', '공부', '놀기']
print(zip(days, doit))
print(list(zip(days, doit)))
print(set(zip(days, doit)))
print(dict(zip(days, doit)))

for yoil, halil in zip(days, doit):
    print(yoil, halil)