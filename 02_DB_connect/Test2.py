# pin = '880122-1234567'
# birthday = '홍길동님 생년월일 : ' + pin[0:6]
# if(pin[8] == 1 or 3): gender = '성별 : 남자'
# else: gender = '성별 : 여자'
# print( birthday )
# print( gender)


# 2번
# a = [1,3,5,4,2]
# a.sort()
# a.reverse()
# print(a)


# 3번
# a = ['독도는','대한민국의','아름다운','섬입니다']
# result = ' '.join(a)
# print( result )

# 4번
# a = (1,2,3)
# a = (1,2,3,4)
# print(a)

# 5번
# a = b = [1,2,3]
# a[1] = 4
# print(b)

# 6번
# star = 1
# while (star < 6):
#     print("*" * star)
#     star += 1

# 7번
kor_score = [77, 88, 76, 44, 56]
math_score = [96, 99, 100, 55, 66]
eng_score = [50,60,70,80,90]
midterm_score = [kor_score, math_score, eng_score]


s1 = list(zip(kor_score, math_score, eng_score))
for i in range(len(s1)):
    print(str(i + 1) + '번 학생 국어 : '+ str(s1[i][0]) + ', 수학 : ' + str(s1[i][1]) + ', 영어 : ' + str(s1[i][2]) + ', 총점 : ' + str(sum(s1[i])), '평균 : ' + str(round(sum(s1[i]) / len(s1[i]), 1)))
# 8번
# life = {
#     'animal': {
#         'cats': {'Kim','Lee','Choi'},
#         'octopi': {},
#         'emus': {}
#     },
#     'plants': {},
#     'other': {}
# }