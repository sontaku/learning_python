data = ['안녕하세요', '감사합니다', '행복하세요']
if len(data) != 0:
    print('있다')
    if data[2][0] == '행':
        print('OK')
    else:
        print('NO')
else:
    print('없다')

print('--------------------------------')

for i in range(len(data)):
    print(str(data[i]))
    if i == len(data) - 1:
        print('안녕히가세요')

print('---------------------------------')

while len(data) != 0:
    newStr = data.pop()
    print(newStr)

print('--------------------------------')
data = ['안녕하세요', '감사합니다', '행복하세요']
a, b, c = data
for text in enumerate(data):
    print(text)

print('--------------------------------')
names = ['홍길동','박길동','김길동']
hello = ['안녕하세요', '감사합니다', '행복하세요']
for text in zip(names, hello):
    print(text)
    
print('-------------------------------')