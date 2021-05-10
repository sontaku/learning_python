# 1
# firNum = int(input('정수를 입력하세요:'))
# secNum = int(input('정수를 입력하세요:'))
# thdNum = int(input('정수를 입력하세요:'))
# fourNum = int(input('정수를 입력하세요:'))
# fivNum = int(input('정수를 입력하세요:'))
# result = (firNum + secNum + thdNum + fourNum + fivNum) / 5
# print('평균=',result)

# 2
# word = input('문자열입력:')
# print('결과 : ', word[::-1])

# 3
# sumList = input('정수리스트입력: ')
# sumList = sumList.split()
# temp = 0
# for i in range(len(sumList)):
#     temp += int(sumList[i])
# print('평균=', temp/len(sumList))

# 4
dt = {
    2:['A','B','C'],
    3:['D','E','F'],
    4:['G','H','I'],
    5:['J','K','L'],
    6:['M','N','O'],
    7:['P','Q','R','S'],
    8:['T','U','V'],
    9:['W','X','Y','Z']}
dtValues = dt.values()
print(dtValues)
ipStr = input('문자열을입력하시오:')

for i in range(len(ipStr)):
    for j in range(len(dtValues)):
        # print(ipStr[i])
        # print(dt[j + 2])
        if ipStr[i] in dt[j + 2]:
            print(dtValues[j])
