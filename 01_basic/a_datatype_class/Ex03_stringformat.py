
# -----------------------------------------
#  문자열 포맷
#       0- 문자열 포맷팅
#               print('내가 좋아하는 숫자는 ', 100 )
#               print('내가 좋아하는 숫자는 ' + 100 ) # 에러 발생
#       1- format() 이용
#               print('내가 좋아하는 숫자는 {0:d} 이다'.format(100) )
#       2- % 사용
#               print('내가 좋아하는 숫자는 %d 이다' % 100 )
#       성능(속도)는 %이 더 빠르다고는 하지만 코드가 깔끔하게 하는 것이 더 중요하다고 하고는
#       어느 것으로 선택하라고는 안 나옴

# [참고] http://pyformat.info

# format() 이용
# java sql의 PreparedStatement와 비슷한 형태
msg = '{1}님, 오늘도 행복하세요 - {0}으로부터'
print(msg.format('홍길동', '씨앗'))

msg = '{name}님, 오늘도 행복하세요 - {group}으로부터'
print(msg.format(name='홍길동', group='씨앗'))

# % 이용 - printf() 역할
name = '홍길동'
age = 22
height = 170.456

print('%s님 %d세이고, 키는 %10.1f cm입니다' % (name, age, height))


#--------------------------------------------------
# 실수인 경우
temp = 99.99
print('숫자 :', temp)
print('숫자 : %.2f' % temp)
print('숫자 : {0:.1f}'.format(temp))


tttt = '가나다 라마 바'
print(tttt.split())