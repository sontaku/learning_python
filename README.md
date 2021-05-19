# learning_python

## 설치



### 1. anaconda 설치

- anaconda는 기본 파이썬 + 기본 패키지 내장 + 에디터 포함
- https://www.anaconda.com/products/individual
- window 64bit 설치
- Anaconda3-2020.11-Windows-x86_64.exe



### 2. 파이썬 버전 확인( Python 3.8.5 )

``` 
python --version
```



### 3. IDE ( Editer )

- pycharm
  - https://www.jetbrains.com/ko-kr/pycharm/download/#section=windows
  - 무료 오픈소스 버전(community) 설치
- jupyter note book (in anaconda)



## 코딩 규칙

```markdown
유명한 개발자 마틴 파울러의 명언
    "컴퓨터가 이해할 수 있는 코드는 어느 바보나 다 짤 수 있다.
    좋은 프로그래머는 사람이 이해할 수 있는 코드를 짠다"
```

### 1. 파이썬 기본 규칙

   - 들여쓰기는 4 스페이스
        - 한 줄은 최대 80자 이내로
        - 불필요한 공백은 피함

### 2. PEP8 규칙 ( 가능하면 지키는 코딩 방식 )

   - = 연산자는 1칸 이상 띄우지 않는다　（적용하지않기로）
        a = 12  ->  a=12
   - 변수명에 소문자 l(엘), 대문자 O(오), 대문자 I (아이)는 금한다
        lIOO = 100  (엘아이오오)
   - 주석은 항상 갱신하고, 불필요한 주석을 지운다
   - 함수명은 소문자로 구성하고 필요하면 밑줄로 나눈다

### 3. 파이썬은 파이써닉하게 코딩하자!

### 4. 파이썬은 파이썬이다.



## 파이썬 특징

### 장점

- 간단하고 배우기 쉬운 언어

  그러나 map, reduce, zip 함수는 다소 난이도 높음

- 인터프리터 언어( 컴파일 X )

  컴파일하지 않고 한 줄씩 읽어들임

- 강력한 외부 라이브러리

- (R에 비해) 범용적 언어

  통계분석 분야 : R언어 -> python 중 pandas로 통계 분야를 다룸



### 단점

- 하드웨어 제어, 반복 연산에 부적절함
- GIL ( Global Interpreter Lock ) : 쓰레드 처리함에 배타적 잠금





## 파이썬 공부법

A 학습 -> B 학습(막힘?무시) -> C 학습 -> A 학습 -> B학습 -> D 학습

단계별로 학습하되, 막힌 부분에 연연하지 말자





## 문법

```python
a = 7
b = 7

print(id(7))
print(id(a))
print(id(b))

print(a is b)
print(7 is a)
```

파이썬에서는 할당하거나 저장한다는 표현보다는 가리킨다고 표현한다.

위의 경우 a와 b와 7은 같은 값을 가리킨다고 볼 수 있다.

주소값 또한 같은 값으로 출력이 된다.



### 파이썬 콘솔의 특성

*파이썬*은 실행시  `-5 ~ 256` 범위에 해당하는 숫자와, 

`[a-zA-Z0-9_]`에 해당하는 char에 대해서는 내부적으로 intern 하고 있다.



여기서 범위는 말그대로 값을 의미한다.



### 변수 삭제

```python
del d
''' d는 변수명 '''
```



### 연산자

파이썬에 증감 연산자(++, --)는 존재하지 않으므로 주의

-------------------

#### 기초 연산자

+, -, *, % 는 자바와 같음

/ : 나누기 (실수값 결과)

// : 나누기 (정수값 결과)

** : 제곱



#### 관계 연산자

<, >, <=, >=, ==, !=



#### 논리 연산자

not, or, and



#### 이진(비트) 연산자

~ : not

| : or

& : and

^ : xor

'<<' : shift

'>>' : shift



#### 대입 연산자

자바와 같음



#### 기타 연산자

is : 비교하는 객체의 주소가 같으면 true

is not : 비교하는 객체의 주소가 다르면 true

in : 요소에 포함되면 true

not in : 요소에 포함되지 않으면 false



#### [참고] 출력 포맷

```python
y = 8.3/2.7
print('y = ', y)
# y =  3.074074074074074

print('실수 : {0}, 정수 : {1}'.format(y, 100))
```



#### 연습문제

```python
1. 변수와 자료형

 

1. 다음 코드의 실행 결과를 쓰시오.

>>> a = 777

>>> b = 777

>>> print(a == b, a is b)



2. 다음 중 변수를 메모리에서 삭제하기 위해 사용하는 명령어는?

➀ del ➁ delete ➂ remove ➃ pop ➄ clear



3. 빈칸에 들어갈 각각의 코드 실행 결과를 쓰시오.

>>> a = 3.5

>>> b = int(3.5)

>>> print(a**((a // b) * 2))

(가) 

>>> print(((a - b) * a) // b)

(나)

>>> b = (((a - b) * a) % b)

>>> print(b)

(다)

>>> print((a * 4) % (b * 4))

(라)



4. 입력받은 섭씨온도를 화씨온도로 변환하는 프로그램을 코딩하려고 한다. 코드 순서를 바르게 나열한 것은?

(1) fahrenheit = (( 9 / 5) * celsius) + 32

(2) celsius = input("섭씨온도를 입력하세요:")

(3) print("섭씨온도:",celsius, "화씨온도:", fahrenheit)

(4) celsius = float(input("섭씨온도를 입력하세요:"))

➀ (2) - (1) - (3)➁ (4) - (3) - (1) ➂ (1) - (2) - (3)

➃ (4) - (1) - (3) ➄ (4) - (2) - (3)



​

5. 다음 변수 a의 자료형은?

a = "True"

➀ 소수형 ➁ 문자형 ➂실수형➃불린형➄ 정수형



​

6. 다음과 같은 코드 작성 시, 실행 결과로 알맞게 짝지어진 것은?

>>> a = 10.6

>>> b = 10.5 

>>> print(a * b)

>>> type(a + b)

➀ 111.3, <class ‘int’>➁ 111.3, <class ‘str>➂ 111.3, <class ‘float’>

➃ 105.0, <class ‘int>➄ 105.0, <class ‘float’>



​

​

7. 다음과 같이 코드를 작성했을 때, 실행 결과로 알맞은 것은?

>>> a = "3.5"

>>> b = 4

>>> print(a * b)

➀ error ➁ 3.53.53.53.5 ➂ 14.0 ➃ 14 ➄ "14"



​

​

8. a = "3.5", b = "1.5"일 때, print(a + b)의 실행 결과는?

① 5 ② 3.51.5 ③ a + b ④ ab➄ 2



​

​

​

9. 다음과 같이 코드를 작성했을 때, 실행 결과로 알맞은 것은?

>>> a = '3'

>>> b = float(a)

>>> print(b ** int(a))

① TypeError ② '27.0' ③ 27.0 ④ 27 ⑤ '27



10. 변수(variable)에 대한 설명으로 틀린 것은?

① 프로그램에서 사용하기 위한 특정한 값을 저장하는 공간이다.

② 선언되는 순간 메모리의 특정 영역에 공간이 할당된다.

③ 변수에 할당된 값은 하드디스크에 저장된다.

④ A = 8은 "A는 8이다"라는 뜻이 아니다.

⑤ ‘2x + 7y’는 14라고 하면, 이 식에서 x와 y가 변수이다.


​

​

​


11. 다음과 같이 코드를 작성했을 때, 실행 결과로 알맞은 것은?

>>> a = '20'

>>> b = '4'

>>> print(type(float(a / b)))

➀<class 'int'>➁<class 'str'>➂<class 'float'>

➃ 4. 3.333333333 ➄TypeError


​

​

​

​

13. 변수명을 지을 때 권장하는 규칙 중 틀린 것은?

① 변수명은 알파벳, 숫자, 언더스코어(_ ) 등을 사용하여 표현할 수 있다.

② 변수명은 의미 있는 단어로 쓰는 것을 권장하며, 한글도 사용할 수 있다.

③ 변수명은 대소문자가 구분된다.

④ 문법으로 사용되는 특별한 예약어는 변수명으로 쓰지 않는다.

⑤ 변수명은 _( 언더스코어) 대신 낙타표시법으로 작성한다.
```



### 문자열 인덱싱

```python
#  (3) 문자열의 인덱싱과 슬라이싱
#       - 인덱스는 0부터 시작한다
#       - s[i] : s 문자열에서 i번째 문자 추출
#       - s[i:j] : s 문자열에서 i번째에서 j-1까지의 문자 추출
#       - s[i:j:k] : s 문자열에서 i번째에서 j-1까지에서 k개씩 건너뛰어 문자 추출
#
#       - s[-i] : s 문자열에서 뒤에서부터 i번째 문자 추출
#                 ( 뒤에서 인덱스는 1부터 센다 )
```



#### 연습

```python
# 1) 5번째부터
print(msg[5:])
# 2) 5번째 전의 문자까지
print(msg[:5])
# 3) 5번째 전의 문자까지에서 2개씩 건너뛰어
print(msg[:5:2])
# 4) 문자열 전체에서 2개씩 건너뛰어
print(msg[::2])
```



#### [참고] 회문 : 문자열을 반으로 접었을때 반복되는 형태

```python
'''
    abcba : 회문
    abcde : 회문 X
    102201 : 회문
'''
```



아래와 같이 알고리즘에서 활용할 수 있다.

```python
s = '1001'
s2 = s[::-1]
if(s == s2):
    print('회문')
else:
    print('회문이 아님')
```



### 문자열 관련 함수

s.count('글') : s 문자열에서 '글'이라는 문자 개수 세기

s.index('글') : s 문자열에서 문자 '글' 위치 알려주기

s.find('글') : s 문자열에서 문자 '글' 위치 알려주기

s.rfind('글') : s 문자열에서 문자 '글' 오른쪽에서 왼쪽으로 찾아서 위치 알려주기

len(s) : s 문자열 길이

s.upper() : 소문자를 대문자로

s.lower() : 대문자를 소문자로

s.lstrip() : 왼쪽 공백 지우기

s.rstrip() : 오른쪽 공백 지우기

s.strip() : 양쪽 공백 지우기

s.replace("a","b")  :  s 문자열에서 단어 a를 단어 b로 바꾸기

s.split() : s 문자열을 공백으로 나누기

s.split('z') : s 문자열을 z 기호로 나누기

d.join(s) : d 단어를 s 문자열에 삽입



#### 연습

```python
msg ='오늘도 행복도 하다'

""" [ 출력결과 ]
    1) '행복'이라는 글자 위치 찾기
    2) '가자'라는 글자 위치 찾기
    3) '행복'이라는 글자를 오른쪽에서 왼쪽으로 찾기
    4) 문자열 전체 길이 구하기
    5) '도'라는 단어의 갯수 구하기
"""
print(msg.index('행복'))
print(msg.find('가자'))
print(msg.rfind('행복'))
print(len(msg))
print(msg.count('도'))


msg = "우리는 독도를 지킨다"
# 1) 독도를 대한민국으로 변경
print(msg.replace('독도', '대한민국'))

# 2) 공백을 기준으로 단어 나누기
print(msg.split(" "))

# 3) 각 단어마다 콤마(,)를 추가
print(','.join(msg))
```



### bool형



### 문자열 포맷

```python
# 0- 문자열 포맷팅
print('내가 좋아하는 숫자는 ', 100 )
print('내가 좋아하는 숫자는 ' + 100 ) # 에러 발생
# 1- format() 이용
print('내가 좋아하는 숫자는 {0:d} 이다'.format(100) )
# 2- % 사용
print('내가 좋아하는 숫자는 %d 이다' % 100 )

# [참고] http://pyformat.info

```



#### format() 이용

```python
msg = '{}님, 오늘도 행복하세요 - {}으로부터'
print(msg.format('홍길동', '씨앗'))

# 출력값 : 홍길동님, 오늘도 행복하세요 - 씨앗으로부터
```

java sql의 PreparedStatement와 비슷한 형태



순서 변경

```python
msg = '{1}님, 오늘도 행복하세요 - {0}으로부터'
print(msg.format('홍길동', '씨앗'))

# 출력값 : 씨앗님, 오늘도 행복하세요 - 홍길동으로부터
```



변수 지정

```python
msg = '{name}님, 오늘도 행복하세요 - {group}으로부터'
print(msg.format(name='홍길동', group='씨앗'))

# 출력값 : 홍길동님, 오늘도 행복하세요 - 씨앗으로부터
```



#### % 이용

```python
name = '홍길동'
age = 22
height = 170.456
print('%s님 %d세이고, 키는 %10.1f cm입니다' % (name, age, height))

# 출력값 : 홍길동님 22세이고, 키는      170.5 cm입니다
```



#### 실수인 경우

```python
temp = 99.99
print('숫자 :', temp)
print('숫자 : %.2f' % temp)
print('숫자 : {0:.1f}'.format(temp))

# 출력값 : 숫자 : 99.99
# 출력값 : 숫자 : 99.99
# 출력값 : 숫자 : 100.0
```



> 문자열 연습문제 : https://cafe.naver.com/javassem?iframe_url=/MyCafeIntro.nhn%3Fclubid=25907255
>
> 
>
> 답
>
> 1. 3
>  문자열 a + 문자열 b
> 2. 2
>  3+5+13 = 21
> 3. 1 (Gachon Human)
> 4. 2
>  원본 그대로
> 5. 1010102
> 6. aa
> 7. 8,1
> 8. 3
> 9. 1



### Date 타입

#### 현재 날짜 출력

```python
import datetime
today = datetime.date.today();
print('today is ', today)

# 출력값 : today is  2021-05-10
```



#### 연도, 월, 일

```python
print('연도: ', today.year)
print('월: ', today.month)
print('일: ', today.day)

# 출력값 : 연도:  2021
# 출력값 : 월:  5
# 출력값 : 일:  10
```



#### 날짜 계산

```python
import date, timedelta

print('어제: ', today + timedelta(days=-1))
print('일주일전: ', today + timedelta(days=7))
print('열흘 후: ', today + timedelta(days=10))

# 출력값 : 어제:  2021-05-09
# 출력값 : 일주일전:  2021-05-17
# 출력값 : 열흘 후:  2021-05-20
```



#### [중요] 날짜 변환

##### 1. date to string

```python
from datetime import datetime
today = datetime.today()
print(today.strftime('%Y-%m-%d %H:%M'))

# 출력값 : 2021-05-10 10:29
```



##### 2. string to date

```python
from datetime import datetime
strToday = '2021-05-10 10:30:30'
print(datetime.strptime(strToday, '%Y-%m-%d %H:%M:%S'))

# 출력값 : 2021-05-10 10:30:30
```



### 자료형

> **list** - > array, ArrayList in java
>
> **set** -> Set in java
>
> **tuple**
>
> **dictionary** -> Map(HashMap) in java



#### list

- 임의의 객체를 순차적으로 저장하는 집합 자료형
- 각 값에 대해 인덱스 부여
- 변경가능 (중요)
- 기호 : 대괄호 [ ] 사용

배열은 연속적으로 공간을 저장하는 것이나, 파이썬에는 없다

파이썬에서는 리스트를 사용한다

배열은 생성시 크기를 지정하지만 리스트는 크기 제한이 없다



##### 기본 리스트 인덱스

```python
arr = [] # 비워져 있는 리스트 생성
arr = [1,2,3,4,5]

arr.append(10)
print(arr)
# 출력값 : [1, 2, 3, 4, 5, 10]
```



##### 이중 리스트

 ```python
 arr = [1, 2, 3, 4, 5]
 arr.append([6, 7, 8])
 print(arr)
 
 # 출력값 : [1, 2, 3, 4, 5, [6, 7, 8]]
 ```



##### List 복사

- 얕은 복사

```python
a = ['a', 'b', 'c']
b = a
print(a is b)
b[1] = 100
print(a)

# 출력값 : True
# 출력값 : ['a', 100, 'c']
```

위의 경우 같은 하나의 주소를 가리킨다.



- 깊은 복사

```python
a = ['a', 'b', 'c']
b = a[:]
print(a is b)
b[1] = 100
print(a)

# 출력값 : False
# 출력값 : ['a', 'b', 'c']
```

깊은 복사는 해당 값을 가져와 새로운 메모리에 할당하여 생성한다.



- copy를 통한 깊은 복사

```python
from copy import copy
b = copy(a)
print(a is b)

# 출력값 : False
```



##### 연습문제

https://cafe.naver.com/javassem?iframe_url=/MyCafeIntro.nhn%3Fclubid=25907255

> 답
>
> 1. [0, 1, 2] [0, 1]
>
> 2. [4, 3, 2, 1, 0]
>
> 3. [['egg', 'salad', 'bread'], ['lamb', 'chicken'], ['apple']]
>
> 4. [1, 2, 3, 4], none
>
>    sort()는 리턴값이 없어서 list_b는 None
>
> 5. ['orange', 'strawberry', 'melon'] ['banana', 'orange']
>
> 6. 1,2,3,4,1,2,3,4
>
> 7. False 6
>
> 8. 4
>
> 9. 3
>     input 함수는 형변환하지 않으면 무조건 스트링으로 반환
>
> 10. ["Korea", "Japan", "China", ["Seoul", [2, 3], "Tokyo", "Beijing"]]	
>
> 11. true, 얕은복사 // false, 같은값 다른객체
>
> 12. 실행시 intern 된 메모리 1을 가리켜 true // 256를 넘어서는 값은 새로운 주소값을 가짐, 각각 선언하여 false
>
> 13. 1
>     리스트 + 리스트 = 리스트





#### set

- 집합에 관련된 자료형
- 순서를 지정하지 않는다
- 중복을 허용하지 않는다
- 기호 : 중괄호 { } 사용

```python
s = set() # 빈 집합을 생성
s = set([1,2,3,1,1])
print(s)
# print(s[0]) # 순서가 존재하지 않아 에러!

# 출력값 : {1, 2, 3}
```



##### 교집합

```python
s = set([1,2,3,1,1])
s3 = {3,4,5,6}
print(s.intersection(s3))

#출력값 : {3}
```



##### 합집합

```python
s = set([1,2,3,1,1])
s3 = {3,4,5,6}
print(s.union(s3))

#출력값 : {1, 2, 3, 4, 5, 6}
```



##### [추가] 차집합 & 여집합

```python
print(s & s3) # 교집합
print(s | s3) # 합집합
print(s - s3) # 차집합
print(s3 - s) # 여집합

#출력값 : {3}
#출력값 : {1, 2, 3, 4, 5, 6}
#출력값 : {1, 2}
#출력값 : {4, 5, 6}
```



#### tuple

- 리스트와 유사하지만 튜플은 값을 변경 못한다.
- 각 값에 대해 인덱스가 부여
- **[중요]변경 불가능**
- 소괄호 () 사용



```python
# (1) 튜플 생성
t = (1,2,3)

# (2) 튜플은 요소를 변경하거나 삭제 안됨
print('------------------- 2 -----------------')
t[1] = 0  # 블럭이 생기면서 실행 안됨
del t[1]   # 에러 발생
del t # 전체삭제

# (3) [_중요_]하나의 요소를 가진 튜플
print('------------------- 3 -----------------')
t3 = (1)
print(t3)
# print(t3[0]) # 에러
print(type(t3)) # <class 'int'>

# 요소가 하나일때는 콤마를 통해 튜플임을 명시
t3 = (1,)
print(t3)
print(type(t3)) # <class 'tuple'>
```



#### dictionary (a.k.a. dict)

- 키와 값으로 구성 ( ***자바의 map과 유사*** )
- 저장된 자료의 순서는 의미 없음
- 중괄호 {} 사용
- 변경가능



- keys() : key만 추출 (임의의 순서)
- values() : value만 추출 (임의의 순서)
- items() : key와 value를 튜플로 추출 (임의의 순서)

##### 생성, 출력

```python
# 생성
dt = {1:'one', 2:'two', '3':'three'}
print(dt)

# 키값이 1인 요소 출력
print(dt[1])

# 키값이 3인 요소 출력 => 존재하지않음
# print(dt[3])

# 키값이 '3'인 요소 출력
print(dt['3'])
```



```python
# 중복값이 있는 경우
dt = {1:'one', 2:'two', '3':'three', 1:'하나'}
print(dt)

# 출력값 : {1: '하나', 2: 'two', '3': 'three'}
```

나중에 선언한 값으로 다시 가리킴(초기화)



##### 값 추가, 수정

```python
# 추가
dt = {1:'one', 2:'two', '3':'three', 1:'하나', 3:'셋'}
dt['korea'] = 'seoul'
print(dt)

# 출력값 : {1: '하나', 2: 'two', '3': 'three', 3: '셋', 'korea': 'seoul'}

# 수정
dt['korea'] = '서울'
print(dt)

#출력값 : {1: '하나', 2: 'two', '3': 'three', 3: '셋', 'korea': '서울'}
```



##### 여러개 삽입(추가)

```python
dt.update({5:'kim', 6:'hong', 7:'kang'})
```



##### Key로 Value값 찾기

```python
print(dt.get(9)) # 존재하지 않으면 None
print(dt.get(9, '없음')) # None -> '없음' 변형
```



##### Key와 Value만 따로 검색

```python
print(dt.keys()) # key값만 가져옴
print(dt.values()) # value 값만 가져옴
print(dt.items()) # key,value 묶음 조회

# 출력값 : dict_keys([1, 2, '3', 3, 'korea', 5, 6, 7])
# 출력값 : dict_values(['하나', 'two', 'three', '셋', '서울', 'kim', 'hong', 'kang'])
# 출력값 : dict_items([(1, '하나'), (2, 'two'), ('3', 'three'), (3, '셋'), ('korea', '서울'), (5, 'kim'), (6, 'hong'), (7, 'kang')])
```



#### 콘솔 입력 처리 함수

- input() : 기본적으로 문자열로 입력받음
- eval() : 함수로 감싸면 숫자 처리됨
- int() / float() / str() 자료형변환  ( eval() 사용보다는 형변환을 권장 )



##### 구구단 예제

```python
# 단을 입력받아 구구단을 구하기
num = input('구구단을 외자~ 구구단을 외자~ 몇 단? : ')
for i in range(1, 10):  # 1 ~ 9
    # print(num, 'x', i, '=', i * int(num))
    print('{} * {} = {}'.format(num, i, int(num) * i))
```



##### 이중 for문

```python
for i in range(5):
    for j in range(5):
        # 연산의 끝마다 ', '를 추가하며 끝부분은 "" 공백만
        print(i * j, end=', ' if j < 4 else "")
    print()
# 출력값 : 
# 0, 0, 0, 0, 0
# 0, 1, 2, 3, 4
# 0, 2, 4, 6, 8
# 0, 3, 6, 9, 12
# 0, 4, 8, 12, 16
```



### 제어문

- 파이썬은 들여쓰기를 하여 블록{}을 대신 표현한다
- 들여쓰기는 탭과 공백을 섞어 쓰지 말자

```python
if a>b:
	print(a)
		print(b)  => 에러발생
```

#### if문

```python
if 조건식A :
	문장들
elif 조건식B :
	문장들
else :
	문장들
```

- 조건식이나 else 뒤에는 콜론(:) 표시
- 조건식은 ( ) 괄호 필요없음
- 실행할 코드가 없으면 pass
- 파이썬은 switch 문 없음



```python
a = 0
if a:
    print('True1')
else:
    print('False1') # False1 출력
```



##### 논리연산자 활용

```python
# (2) 논리연산자 이용한 조건
a = 10
b = -1
if a and b:
    print('True2') # True2 출력
else:
    print('False2')

if a or b:
    print('True3') # True3 출력
else:
    print('False3')
    
# [참고] 자바의 short circuit logic
print(a and b) # -1 출력
print(a or b) # 10 출력
```



##### if문 로직 연습

```python
word = 'korea'
print(word.find('k')) # 찾아서 0 -> False
if word.find('k'):
    print('1>' + word)

print(word.find('z')) # 못찾아서 -1 -> 있는값이라고 판단해 True
if word.find('z'):
    print('2>' + word)
```



#### for문

```python
for <타겟변수> in 집합객체 :
	문장들
else:
	문장들
# 반복문 뒤에 else는 반복하는 조건에 만족하지않으면 실행
```

집합객체에 해당하는 요소

- 리스트
- 문자열
- 튜플
- 딕셔너리

숫자형은 반복이 되지 않아 집합객체에 들어갈 수 없다.



##### for문 (dict)

```python
e = dict(k=5, j=6)       # 딕셔너리

for k, val in e.items():
    print('key :', k, ', value:', val)
  
# 출력값 :
# key : k , value: 5
# key : j , value: 6
```



#### while문

```python
while 조건문 :
	문장들
else :
	문장들
```



##### 예제

```python
a = ['a', 'b', 'c']
while a: # 조건
    data = a.pop()
    print(data)
else: # for문이나 와일문 조건문에 위배됐을때
    print('끝')
   
# 출력값 : 
# c
# b
# a
# 끝
```



#### 요소 분할 (unpacking)

```python
msg = '행복해'            # 문자열
li = ['a','b','c']       # 리스트
tpl = ('ㄱ','ㄴ','ㄷ')    # 튜플
di = {'k': 5, 'j': 6, 'l':7 }    # 딕셔너리

# unpacking : 요소분할
c1, c2, c3 = li
print(c1)
print(c2)
print(c3)

# 출력값 : 
# a
# b
# c
```



예제

```python
'''
    [출력결과]
    1 + 2 = 3
    3 + 4 = 7
    5 + 6 = 11
'''
for i, j in alist:
    print('{} + {} = {}'.format(i, j, i + j))
```



#### enumerate()

> java의 iterator와 비슷한 성격

```python
user_list = ['개발자', '코더', '프로그래머']
for val in user_list:
    print(val)
# 출력값 : 
#개발자
#코더
#프로그래머

for val in enumerate(user_list):
    print(val)
# 출력값 : 
#(0, '개발자')
#(1, '코더')
#(2, '프로그래머')

for idx, val in enumerate(user_list):
    print(idx, '>', val)
# 출력값 : 
#0 > 개발자
#1 > 코더
#2 > 프로그래머
```



#### [중요] zip()

자료형 크기에 상관없이 1:1 iterator 활용

```python
days = ['월', '화', '수']
doit = ['잠자기', '밥먹기', '공부', '놀기']

print(zip(days, doit)) 
# <zip object at 0x000002AEF85063C8>

print(list(zip(days, doit)))
# [('월', '잠자기'), ('화', '밥먹기'), ('수', '공부')]

print(set(zip(days, doit)))
# {('수', '공부'), ('월', '잠자기'), ('화', '밥먹기')}
# set의 경우 월,화,수 순서대로 삽입됐지만 순서가 없어 '가나다'순으로 조회됨

print(dict(zip(days, doit)))
# {'월': '잠자기', '화': '밥먹기', '수': '공부'}
```



활용예제

```python
test=dict(zip(days, doit))
print(test['월'])

# 잠자기
```

위와 같이 객체로 활용가능



##### for문 활용

```python
for yoil, halil in zip(days, doit):
    print(yoil, halil)
    
# 출력값 : 
# 월 잠자기
# 화 밥먹기
# 수 공부
```



#### comprehension

- 하나 이상의 이터레이터로부터 파이썬 자료구조를 만드는 컴팩트한 방법
- 비교적 간단한 구문으로 반복문과 조건 테스트를 결합



##### [중요] list cprhs

[ 표현식 for 항목 in 순회가능객체 ]

[ 표현식 for 항목 in 순회가능객체 if 조건 ]

for문이 먼저 돌고 for문 앞 연산 진행

```python
# [중요]
# 1~6 정수를 하나씩 n에 넣고, n을 b리스트 요소로 지정
blist = [n for n in range(1, 7)]

# n의 2배수를 요소로 지정
blist = [n * 2 for n in range(1, 7)]

# n이 홀수인 값을 n+1에 담아 요소로 지정
blist = [n + 1 for n in range(1, 7) if n % 2 == 1]
```



###### [참고] 사용 vs 미사용

```python
# [참고] comprehension 미사용시
clist = []
for r in range(1, 4):
    for c in range(1, 3):
        clist.append((r, c))
print(clist)

# 사용시
clist = [(r, c) for r in range(1, 4) for c in range(1, 3)]
print(clist)
```

이중 for문의 경우 앞의 for문을 바깥에서 먼저 실행하는 구조



##### dictionary cprhs

{ 키_표현식: 값_표현식 for 표현식 in 순회가능객체 }

```python
data = (2, 3, 4)
adic = {n: n ** 2 for n in data}
print(adic)

# 출력값 : {2: 4, 3: 9, 4: 16}
```



###### 예제

```python
word = 'LOVE LOL'
wcnt = {n: word.count(n) for n in word}
print(wcnt)

# 출력값 : {'L': 3, 'O': 2, 'V': 1, 'E': 1, ' ': 1}
```



##### set cprhs

 { 표현식 for 표현식 in 순회가능객체 }

```python
data = [1,2,3,1,1,2]
aset = {n for n in data}
print(aset)

# 출력값 : {1, 2, 3}
```

중괄호로 감싸 set 자료형으로 요소 지정



##### *generator* cprhs

```python
data = [1,2,1,2,3,2,1]

glist = (n for n in data)
print(type(glist))
print(list(glist))

# 출력값 : <class 'generator'>
# 출력값 : [1, 2, 1, 2, 3, 2, 1]
```

소괄호() 를 사용하면 튜플이라 생각하지만 튜플은 컨프리핸션이 없다.



### 함수

```python
def func():
    print('inside func')
    
func()
# 출력값 : inside func

# 리턴값이 없어 None도 출력
print(func())
```



#### 리턴값이 있는 함수

```python
def func(arg1, arg2):
    return arg1 + 100, arg2 + 10

result = func(1, 2)
print(result)

# 출력값 : (101, 12)
```





#### 여러개의 리턴값이 있는 함수

> 튜플로 하나의 리턴

```python
def func(arg1, arg2):
    return arg1 + 100, arg2 + 10

res1, res2 = func(1,2)
print(res1, res2)

# 출력값 : 101 12
```



#### 위치 인자 vs 키워드 인자

> ```
> positional argument : keyword argument
> ```



##### 위치 인자 ( positional argument )

```python
def func(greeting, name):
    print(greeting, '!!!!', name, '님')

func('안녕', '홍길동')
func('김길동', '잘가')

# 출력값 : 안녕 !!!! 홍길동 님
# 출력값 : 김길동 !!!! 잘가 님
```

위치인자 함수의 경우 원하는곳에 데이터가 삽입되기 보다는 순서대로 매개변수를 받아 처리한다.



##### 키워드 인자 ( keyword argument )

```python
func(name='김길동', greeting='잘가')

# 출력값 : 잘가 !!!! 김길동 님
```

키워드 인자의 경우 함수를 사용할때 미리 '함수의 파라미터명'과 일치시켜준다.



#### 인자의 기본값 지정

```python
def func(greeting, name='홍길동'):
    print(greeting, '!!!!', name, '님')

func('헬로우', '존')
func('올라')

# 출력값 : 
# 헬로우 !!!! 존 님
# 올라 !!!! 홍길동 님
```

함수 선언시 파라미터의 기본값을 지정해주면, null 값을 전달받아도 처리할 수 있게 된다.

즉, 기본값은 null값을 전달받을 때만 유효한 값이다.



##### [참고] 기본값 알쓸신잡

```python
def buggy(arg, result=[]):
    result.append(arg)
    print(result)
buggy('가')
buggy('나')
buggy('다', [1,2,3,4])
buggy('라')
```

 위 함수의 경우 result 파라미터는 두번째 인자를 받지 않았을때, 빈 list 객체를 생성 후 처리한다.



```python
# 출력값 : 
['가']
['가', '나']
[1, 2, 3, 4, '다']
['가', '나', '라']
```

세번째의 경우 함수에서 파라미터를 받아 새로운 list 객체를 생성하였지만

파라미터가 없는 경우..



<hr>

#### [중요] 위치 인자 모으기

> ```
> 첫번째와 두번째는 인자가 반드시 들어가고 
> 세번째는 인자가 들어갈 수도 있고 없으면 0으로 초기화한다
> 
> 그러나 네번째 인자부터는 정확히 모른다면?
> ```



```python
def func(a, b, c=0, *args): # args는 변수명
    sum = a + b + c
    for i in args:
        sum += i
    return sum
```

4번째 변수 부터는 파라미터가 몇 개가 들어오든 **튜플**로 변환하여 값을 받는다.

조커와 같은 개념으로 변수명 앞에 *****(별표)를 붙여 표기한다.



```python
print(func(4, 5))
print(func(4, 5, 6))
print(func(4, 5, 6, 7))
print(func(4, 5, 6, 7, 8, 9))  # args에 7,8,9가 튜플로 들어간다

# 출력값 :
9
15
22
39
```



<hr>

#### [중요] 키워드 인자 모으기

- *변수명 : 위치인자 모으기
- **변수명 : 키워드인자 모으기
- **dictionary**로 변환하여 값을 받는다.

```python
def func(a, b, c=0, *args, **kwargs):
    sum = a + b + c
    for i in args:
        sum += i
    for k in kwargs:
        sum += kwargs[k]
    return sum

print(func(4, 5, kor=5, eng=10))
print(func(4, 5, 6, kor=5, eng=10))
print(func(4, 5, 6, 7, 8, 9, java=5, python=10))

# 출력값 : 
24
30
54
```

문법상 * 한개짜리를 앞에 써야함



#### 함수의 객체화

> 파이썬에서는 함수도 객체이다.
>
> 아래와 같이 이름 호출을 통한 함수 사용이 가능하다.

```python
def case1():
    print('case-1')

def case2():
    print('case-2')

def case3():
    print('case-3')

# 'a1'는 문자열
# case1은 함수 객체
f = {'a1' : case1, 'a2' : case2, 'a3' : case3} 
print(f['a1'])
f['a1']()

# 출력값 : 
<function case1 at 0x00000174CDD93798>
case-1
```



#### 전역 변수와 지역 변수

자바에서는 블록단위로 전역변수, 지역변수를 분류했는데,

파이썬에서는 *함수단위*로 기준을 나눈다.

```python
temp = '전역 변수'
def func():
    # print('0>', temp) # 전역 변수 호출 불가
    temp = '지역 변수'
    print('1>', temp)
func()
print('2>', temp)

# 출력값 :
1> 지역 변수
2> 전역 변수
```



##### 함수 안에서 전역변수 선언

```python
temp = '전역 변수'
def func():
    global temp # 변수 초기화
    temp = '지역 변수'
    print('1>', temp)
func()
print('2>', temp)

# 출력값 : 
1> 지역 변수
2> 지역 변수
```



#### 람다 함수

```python
# 기존 함수 형태
def f(a, b):
    return print(a + b)
f(3,2)

# 람다
f = lambda a, b : print(a+b)
f(3,2)
```



#### map()

- 연속 데이터를 저장하는 시퀀스 자료형에서 요소마다 같은 기능을 적용할 때 사용
- 형식 : **map(함수명, 리스트형식의 입력값)**
  - 람다 또한 함수의 형태이기에 삽입 가능
- 파이썬 3.x에서는 list(map(calc, ex)) 반드시 list를 붙여야 리스트 형식으로 반환된다
- 파이썬 2.x에서는 list 없이도 리스트 형식으로 반환

```python
def cals(x):
    return x * 2
data = [1, 2, 3, 4, 5]

print(list(map(cals, data)))

# 출력값 :
[2, 4, 6, 8, 10]
```



#### reduce()

리스트 같은 시퀀스 자료형에 차례대로 함수를 적용하여 모든 값을 통합하는 함수

```python
reduce(함수, 순서형 자료)
```

```python
from functools import reduce
data = [1, 2, 3, 4, 5]
def f(a, b):
    return a + b
print(reduce(f, data))

# 출력값 : 15
```



### 모듈(import)

- 함수나 클래스들의 파일
- 모듈이름은 py 확장자를 제외한 파일 이름
- 패키지가 디렉토리라면, 모듈은 파일이다

```python
# mymodule.py
# 참조할 모듈 파일
from random import choice

def get_weather():
    today = ['맑음','비','눈','폭우','돌풍','따뜻']
    return choice(today)

def get_date():
    today = ['월','화','수','목','금','토','일']
    return choice(today)
```

얘는 걍 정리안해야지..



### 클래스

#### 생성자

```python
class Sample:
    data = "헬로우"

    # 생성자
    # self.변수명 -> 멤버변수
    def __init__(self, name):
        self.name = name

# 객체 생성
s = Sample('홍길동')
print(s.name)
```

- `__init__` 함수 : 객체 초기화 함수( 생성자 역할 )
- `self` : 객체 자신을 가리킨다.



#### 소멸자

- 생성자는 프로그램 시작시 자동 실행되듯, 소멸자는 종료직전 실행된다.
- 이를 강제적 실행시키는 방법도 있다.

```python
# 소멸자
def __del__(self):
	self.name = ''
    self.age = 0
    print('__del_- 호출')

# 객체 생성
s = Sample('홍길동', 24)
del s # 객체 삭제
```



#### 인스턴스 함수

> 'self'인 인스턴스를 인자로 받고 인스턴스 변수와 같이 하나의 인스턴스에만 한정된 데이터를 생성, 변경, 참조

```python
class Book:
    # 멤버변수
    cnt = 0
    def __init__(self, title):
        self.title = title

    # 인스턴스 함수
    @classmethod # 자바의 스태틱(메모리 공유)
    def output(self):
        # print('제목은 : ', self.title)
        self.cnt += 1
        print('총갯수 : ', self.cnt)
        
a = Book('책제목이다')
b = Book('두번째책')
c = Book('세번째책')
d = Book('네번째책')
e = Book('다섯번째책')

a.output()
b.output()
c.output()
d.output()
e.output()
```

위의 코드 진행시 cnt 변수는 클래스 변수로 취급되어 누적 값을 갖는다.



#### 클래스 상속

- 파이썬은 method overriding은 있지만 method overloading 개념은 없다
- 파이썬은 다중상속이 가능
- 부모 클래스가 2개 이상인 경우 먼저 기술한 부모클래스에서 먼저 우선 해당 멤버를 찾음

```python
class Animal:
    def move(self):
        print('동물은 움직인다')

# Wolf 클래스는 Animal 클래스 상속관계
class Wolf(Animal):
    def move(self):
        print('늑대는 네발로 달린다')

class Human(Animal):
    def move(self):
        print('사람은 두발로 걷는다')
        
a = Animal()
a.move()

w = Wolf()
w.move()

h = Human()
h.move()
```



##### 다중 상속

```python
class Werewolf(Wolf, Human):
    def move(self):
        # 부모의 move() 호출
        # 2개로부터 상속받았다면 앞의것을 호출한다
        super().move()
        print('늑대인간은 두발로, 네발로 모두 달릴수 있다')
        
w = Werewolf()
w.move()
```



#### 매직 메소드

##### 1. Binary Operators

| Operator |                 Method                  |
| :------: | :-------------------------------------: |
|    +     |      `object.__add__(self, other)`      |
|    -     |      `object.__sub__(self, other)`      |
|    *     |      `object.__mul__(self, other)`      |
|    //    |   `object.__floordiv__(self, other)`    |
|    /     |      `object.__div__(self, other)`      |
|    %     |      `object.__mod__(self, other)`      |
|    **    | `object.__pow__(self, other[, modulo])` |
|    >>    |    `object.__lshift__(self, other)`     |
|    <<    |    `object.__rshift__(self, other)`     |
|    &     |      `object.__and__(self, other)`      |
|    ^     |      `object.__xor__(self, other)`      |
|    \|    |      `object.__or__(self, other)`       |

##### 2. Comparison Operators

더 이상의 자세한 설명은 생략한다.

##### 3. Extended Assignments

##### 4. Unary Operators



##### 예제

```python
class Sample:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 매직 메소드
    def __str__(self):
        return ('이름 : {} \n나이 : {}\n'.format(self.name, self.age))

s = Sample('홍길동', 25)
print(s)
```



### 예외 처리

- 에러

  문법적 오류

- 예외

  실행시 발생하는 오류로 예외가 발생하면 프로그램이 비정상 종료된다



#### 문법

```python
try:
	예외 발생 가능 문장들
except Exception as e: # e는 별칭
	예외가 발생한 후에 실행할 문장들
else:
	예외가 발생하지 않았을 때 실행되는 문장들
finally:
	예외 발생 여부와 상관없이 무조건 실행되는 문장들
```

[참고] 파이썬 내장 예외
        https://docs.python.org/3/library/exceptions.html



### 파일 읽고 쓰기

- 파일을 읽고 쓰기 전에 파일을 열어야 한다

- fileObj = open ( filename, mode )
        mode 첫번째 글자 - 작업 표시
        **r(read)  : 파일 읽기
        w(write) : 파일 쓰기 ( 파일이 없으면 생성하고 파일이 있으면 덮어쓴다 )
        x(write) : 파일 쓰기 ( 파일이 없을 때만 생성하고 쓴다 )
        a(append) : 파일 추가 ( 파일이 있으면 파일의 끝에서부터 추가하여 쓴다 )**

    ​	mode 두번째 글자 - 파일 타입
    ​	t : 텍스트(text) 타입 ( 기본값 )
    ​	b : 이진(binary) 타입
    ​	두번째 글자가 없으면 텍스트 타입이다.

    ​	encoding='utf-8' : 한글

- 파일을 열고 사용 후에는 반드시 닫아야 한다

```python
try:
    f = open('./data/data.txt', 'r', encoding='UTF-8')
except FileNotFoundError as e:
    print(e, '파일을 찾을 수 없습니다')
else:
    while True:
        line = f.readline()
        if not line: break
        print(line)
    f.close()
```



##### with 문

```python
# with 구문 : close() 자동
with open('./data/data.txt', 'r', encoding='UTF-8') as f:
    while True:
        line = f.readline()
        if not line: break
        print(line, end='')
```



### 경로 지정

#### 해당 경로와 하위 목록 확인

```python
from pathlib import Path
'''
 import pathlib 만 선언하면
 Path클래스 사용시 pathlib.Path라고 명시해야 한다. 
'''

# 점 1개는 현재경로
# 점 2개는 상위경로임을 확인 가능하다
p = Path('.')
print(p)
print(p.resolve())  # 현재 패키지 경로를 가리킴 즉, 실제 절대경로
```



```python
test = []

# 현재경로의 하위경로를 iterator로 잡아줌
# for d in p.iterdir():
#     # 디렉토리만 잡아줌
#     if d.is_dir():
#         test.append(d)
# print(test)

test = [d for d in p.iterdir() if d.is_dir()]
print(test)
```



##### 특정 파일명 혹은 확장자 별 처리

```python
p = Path('..') # f_path_class
# glob : 파일 같은 애를 한꺼번에 처리
i = list(p.glob('**/a_datatype_class/*.py'))
print(i)
```



#### 순수 경로

- Path는 파일 시스템에 접근하기 때문에, 기본적으로 운영체제 상에 조작 대상 파일 경로가 존재해야 합니다.
- PurePath는 순수 경로의 기반 클래스입니다.
- 파일 시스템에 접근하지 않기 때문에, ***운영체제 상에 존재하지 않는 파일 경로***를 다룰 수도 있습니다.

##### 존재하지 않는 경로

```python
from pathlib import PurePath

p = PurePath('babo/myclass/myjob')
print(p)
```

실제로 존재하는 경로가 아니기에 **이름만 관리하는 작업**시 사용된다.



##### 사용 예시

```python
p = PurePath('\\192.168.40.55\imsi\mywork')
print(p.parts)
```



##### 경로 붙이기

```python
b = PurePath('mywork')
c = b / 'imsi' / 'test' / 'temp'
print(c)
```



##### 부모경로 찾기

```python
j = PurePath('C:\Windows\System32\drivers\etc\hosts')
print(j.parts)
print(j.parts[3])

print(j.parent)
print(j.parents)
print(j.parents[0]) # 인덱스가 커질수록 상위경로
print(j.parents[1])
print(j.parents[2])

# 출력값 :
('C:\\', 'Windows', 'System32', 'drivers', 'etc', 'hosts')
drivers
C:\Windows\System32\drivers\etc
<PureWindowsPath.parents>
C:\Windows\System32\drivers\etc
C:\Windows\System32\drivers
C:\Windows\System32
```



#### 경로 생성

##### 경로의 상태보기

```python
from pathlib import Path

print(Path.cwd()) # 리눅스의 pwd
print(Path.home()) # 리눅스의 홈디렉토리

p = Path('Ex03_createPath.py')
print(p.stat()) # 리눅스 stat
```



##### 경로 생성시간 

```python
from datetime import datetime
tm = p.stat().st_atime
print(tm)
print(datetime.fromtimestamp(tm))
```



##### 디렉토리 생성

```python
p1 = Path('imsi')
p1.mkdir(exist_ok=True) # 이미 존재해도 생성

# 다중 경로 생성
p3 = Path('imsi2/temp2/test')
p3.mkdir(parents=True)
```



##### 파일 생성

```python
# 1
with open('imsi/1.txt', 'wt', encoding='UTF-8') as f:
    f.write('오늘도화이팅')

# 2
p = Path('imsi/2.txt')
with open(p, 'wt', encoding='UTF-8') as f:
    f.write('오늘도화이팅')
    
# 3
p = Path('imsi/3.txt')
p.write_text('주말행복', encoding='utf-8')
```



##### 경로 변경

```python
from pathlib import Path
import os

print(Path.cwd()) # 현재 경로

# 체인지 디렉토리
os.chdir('..')
print(Path.cwd()) # 현재 경로의 상위 경로
```



##### 경로 제거

```python
f = Path('imsi/3.txt')
f.unlink()

# 자식으로 파일or디렉토리가 있으면 삭제 불가
p = Path('imsi')
p.rmdir()
```



##### shutil 라이브러리

```python
# 강제 삭제
import shutil
shutil.rmtree('imsi')

# 파일 복사
shutil.copy('Ex00.txt', 'babo.txt')

# 디렉토리 복사
shutil.copytree('../f_path_class', 'temp')
```



<hr>

## DB 연결

1. 연결객체(Connection) 얻어오기
2. 커서(Cursor) 얻어오기
3. SQL 문장
4. SQL 실행
5. 커서 닫기
6. 연결 닫기



### 예제

```python
# 1) 연결객체(Connection) 얻어오기
import cx_Oracle as oci
conn = oci.connect('SCOTT/TIGER@127.0.0.1:1521/xe')
print('연결 성공', conn.version)

# 2) 커서(Cursor) 얻어오기
cursor = conn.cursor()

# 3) SQL 문장
sql = 'SELECT * FROM emp'

# 4) SQL 실행
cursor.execute(sql)
# 결과처리
# 4-1) 커서에서 데이터 가져오기
# for rows in cursor:
#     print(rows)
#     print(rows[0], rows[1], rows[2])

# 4-2) 리스트 형식 가져오기
datas = cursor.fetchall()
print(datas)
print(type(datas))
for rows in datas:
    print(rows)
    print(rows[0], rows[1], rows[2])

# 5) 커서 닫기
cursor.close()

# 6) 연결 닫기
conn.close()
```





## 웹 크롤링

### scraping vs crawling

허락 없이 가져다 쓰면 스크래핑

특정 데이터 추출 - 스크래핑



사이트에서 제공해 주는 것을 받아다 처리하면 크롤링



웹 크롤링은 일반적으로 Google, Yahoo, Bing 등이 어떤 종류의 정보를 검색하는 방식

웹 스크래핑은 주식 시장 데이터, 비즈니스 리드, 공급업체 제품 스크래핑과 같은 특정 데이터에 대한 특정 웹 사이트를 대상으로 한 것



### 웹 요청 라이브러리

- requests
  - 외부 라이브러리
  - 인터프리터 추가
- urllib



### requests

> 외부 라이브러리 requests

```python
import requests
# 아래방식은 get 방식
url = 'https://www.google.com'
res = requests.get(url)
# print(res) # 200은 성공 // 405는 에러

# print(res.content)
print(res.text) # utf-8로 인하여 text 방식 권장
print('-' * 50)
```



### urllib

> 내장모듈 urllib 이용

```python
# 내장모듈 urllib 이용
from urllib import request # s 안 붙음

url = 'http://www.google.com'

site = request.urlopen(url)
print(site)
page = site.read()
print(page)
```



### [중요] requests vs urllib(내장모듈) 차이점

> |                  | requests        | urllib                         |
> | ---------------- | --------------- | ------------------------------ |
> | 데이터 전송 형태 | 딕셔너리        | 인코딩하여 바이너리            |
> | 요청 메소드 명시 | get, post...etc | 데이터의 여부에 따라 get, post |
> | 없는 페이지 요청 | 에러X           | 에러O                          |
> | 모듈             | 외장            | 내장                           |
>
> * 어떤 상황에 무엇을 사용해야 하는가...?



#### urlretrieve()

> 웹 상 데이터(주로 이미지)를 로컬에 저장 후 다룰 때 사용
>
> **메모리에 올리지 않고** 파일에 저장

```python
from urllib import request as req

url = 'http://www.google.com'
fileName = 'data/google.html'
req.urlretrieve(url, fileName)
print('저장됨')
```

위의 fileName은 수동생성



#### urlopen()

> 파일로 바로 저장하기 않고 **메모리에 로딩**

```python
from urllib import request as req

url = 'https://t1.daumcdn.net/daumtop_chanel/op/20200723055344399.png'
fileName = 'data/daum2.png'

site = req.urlopen(url)
down = site.read()

# 메모리의 파일을 저장
with open(fileName, 'wb') as f:
    f.write(down)
```



#### parse.urljoin()

> 상대경로를 절대경로로 변화하는 함수

```python
from urllib.parse import urljoin
baseurl = 'http://www.example.com/html/a.html'

# http://www.example.com/html/b.html
print(urljoin(baseurl, 'b.html'))

# http://www.example.com/html/sub/c.html
print(urljoin(baseurl, 'sub/c.html'))

# http://www.example.com/sub/d.html
# 상대경로 지정으로 최상위 경로로 이동
print(urljoin(baseurl, '/sub/d.html'))

# http://www.example.com/sub/e.html
print(urljoin(baseurl, '../sub/e.html'))

# http://www.example.com/temp/f.html
print(urljoin(baseurl, '../temp/f.html'))

print('---------------------------------')

print(urljoin(baseurl, 'www.other.com/mypage')) # 미완성 경로
print(urljoin(baseurl, '//www.other.com/mypage')) # 완성 경로
print(urljoin(baseurl, 'http://www.other.com/mypage')) # 완성 경로
```

// 슬래쉬 2개를 기준으로 완성된 경로로 분류



### Web api 예제

```python
"""
    전세계날씨제공 API : http://openweathermap.org

    1. 회원가입 : 메뉴 > Sign Up > 사용용도 : Education > 대충가입 (무료는 1번에 60번 호출 가능 )
    2. 개발자모드 : Sign In > API Keys 에서 내가 발급받은 키 (추가 키 가능)
    3. 발급받고 바로 지정 안됨 (시간소요)
"""

# API 키를 지정합니다. 자신의 키로 변경해서 사용해주세요.
apikey = "1db47184ebbc18af53fd996be840d270" # 임시 강사님 key

# 날씨를 확인할 도시 지정하기
cities = ["Seoul,KR", "Tokyo,JP", "New York,US"]

# url 지정
api = "http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}"

# 켈빈 온도를 섭씨 온도로 변환하는 함수
k2c = lambda k: k - 273.15

import requests
for cname in cities:
	url = api.format(city=cname, key=apikey)
    res = requests.get(url)
    print(res.text)
    # print(type(res.text)) # str
    data = json.loads(res.text)

	# 결과 처리
    print('======= 도시 : ', data["name"] + ' =======')
    print('날씨 : ', data["weather"][0]["main"])
    print('온도 : ', k2c(data["main"]['temp']))

    # 최저온도, 최고온도, 기압, 풍속
    print('최저온도 : ', k2c(data["main"]['temp_min']))
    print('최고온도 : ', k2c(data["main"]['temp_max']))
    print('기압 : ', data["main"]['pressure'])
    print('풍속 : ', data["wind"]['speed'])
```



### beautifulsoup4

> 웹에서 가져온 HTML코드를 파이썬에서 사용하기 편하게 **파싱**해주는 라이브러리



#### element

```python
from bs4 import BeautifulSoup

html = """
    <html><body>
        <h1>스크레이핑 연습</h1>
        <p>웹페이지 분석하자</p>
        <p>데이타 정제하기</p>
    </body></html>
"""

# 1. 데이타 파서하기
bs = BeautifulSoup(html, 'html.parser')
# 2. 원하는 요소 접근하기
print('===============================')
p = bs.find('p')
print(p)

h1 = bs.html.body.h1
print(h1)

# 3. 요소의 내용 추출하기
# p = bs.findAll('p')
# print(p)
print('===============================')
pp = bs.find_all('p')
print(pp[1].text)
```



#### attribute

```python
from bs4 import BeautifulSoup

html = """
    <html>
        <body>
            <ul>
                <li><a href='http://www.naver.com'>네이브</a></li>
                <li><a href='http://www.daum.net'>다아음</a></li>
            </ul>
        </body>
    </html>
"""

''' 리스트(li)목록의 내용과 해당 경로를 추출하기
    속성추출 : attrs['속성명']

    [출력결과]
    네이브 : http://www.naver.com
    다아음 : http://www.daum.net
'''
from bs4 import BeautifulSoup

# 1. 데이타 파서하기
bs = BeautifulSoup(html, 'html.parser')

# pp = bs.html.body.ul.li.a
pp = bs.find_all('li')
print(pp)

for i in pp:
    print(i.a.text, " : ",i.a.attrs['href'])

print('==========================')

pp = bs.find_all('a')
print(pp)

for i in pp:
    print(i.text, " : ",i.attrs['href'])
```



#### selector

> jQuery 코드 사용

```python
from bs4 import BeautifulSoup

html = """
    <html><body>
        <div id='course'>
            <h1>빅데이터 과정</h1>
        </div>
        <div id='subjects'> 
            <ul class='subs'>
                <li>머신러닝</li>
                <li>데이터 처리</li>
                <li>데이타 분석</li>
            </ul>
        </div>
    </body></html>
"""

# 파싱
bs = BeautifulSoup(html, 'html.parser')

# (1) id값으로 검색
h1 = bs.select_one('#course > h1')
print(h1)

# (2) class로 검색 - 목록내용 추출
print('=====================')
cls = bs.select_one('.subs')
print(cls)
```



### 연습 예제

```python
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib import request as req

# 교보문고 > '파이썬' 검색 > 국내도서
html = urlopen("http://www.kyobobook.co.kr/search/SearchKorbookMain.jsp?vPstrCategory=KOR&vPstrKeyWord=python&vPplace=top")
# html = urlopen("https://search.kyobobook.co.kr/web/search?vPstrKeyWord=python")

bs = BeautifulSoup(html, 'html.parser')

# -------------------------------------
# 책 제목 추출, 총 권수 출력
titles = bs.select('div.title > a > strong')
# prices = bs.select('div.title > a > sell_price')
print(titles)
for i in titles:
    # print(i.text)
    print(i.string.strip())
print('총 권수 : ', len(titles))

# ----------------------------
# 이미지 다운받아 파일 저장
print('----------------------------------')
imgUrl = bs.select('.cover > a > img')
# print(imgUrl)

for i in range(len(imgUrl)):
    # print(imgUrl[i].attrs['src'])
    imgPath = imgUrl[i].attrs['src']
    imgName = imgUrl[i].attrs['alt'].replace(':', '-')
    print(imgPath + " : " + imgName)
    req.urlretrieve(imgPath, 'images/' + imgName + '.jpg')
```



### 내부 링크 추출

```python
from bs4 import BeautifulSoup
from urllib import parse
from urllib import request

def enum_links(html,base):
    bs = BeautifulSoup(html, 'html.parser')
    links = bs.select('a')
    #-------------------------------------
    result = []
    for a in links:
        href = a.attrs['href']
        url = parse.urljoin(base, href)
        result.append(url)
    return result

if __name__ == '__main__':
    url = 'https://docs.python.org/3.7/library/'
    response = request.urlopen(url)   # urllib.request.urlopen() : BeautifulSoup을 통해 html 파서할(데이타를 가져올) 대상
    result = enum_links(response, url)
    print(result)
```



### 파일 다운

```python
from urllib import parse
from urllib import request
import os, time, re  # re : 정규식

def download_file(url):
    p = parse.urlparse(url)
    print('1>', p)
    savepath = './' + p.netloc + p.path
    print('2>', savepath)
    # 마지막에 '/'로 끝나면 뒤에 index.html 붙이기
    if re.search('/$', savepath):
        savepath += 'index.html'
        print('3>', savepath)
    else:
        savepath += '.html'

    # 해당 파일이 존재하는지
    if os.path.exists(savepath):
        return savepath

    # 다운로드 할 폴더 생성
    savedir = os.path.dirname(savepath)
    if not os.path.exists(savedir):
        os.makedirs(savedir) # dirs 는 하위 경로까지 생성

    # 해당 url을 다운받기
    try:
        print('다운로드 : ', url)
        request.urlretrieve(url, savepath)
        time.sleep(2)
        return savepath
    except:
        print('다운로드 실패 : ', url)
        return None
if __name__ == '__main__':
    # url 지정
    # url = 'https://docs.python.org/3.6/library/'
    url = 'https://search.naver.com/search.naver?where=nexearch&sm=tab_opt&query=%EB%A6%AC%EB%B2%84%ED%92%80+%EB%B9%85%ED%81%B4%EB%9F%BD+%EC%95%84%EB%8B%88%EC%95%BC&nso=so%3Add%2Cp%3A1h&nso_open=1'
    result = download_file(url)
    print(result)
```



## Selenium

- 주로 웹앱을 테스트하는데 이용하는 프레임워크
- 웹 브라우저를 원격으로 조작할 때 사용
- 자동으로 URL을 열고 클릭, 스크롤, 문자 입력등의 동작을 조작할 수 있다.
- webdriver라는 API를 통해 운영체제에 설치된 Chrome등의 브라우저를 제어하게 된다.

Selenium은 driver객체를 통해 여러가지 메소드를 제공한다.

HTML을 브라우저에서 파싱해주기 때문에 굳이 Python와 BeautifulSoup을 사용하지 않아도 된다.



### 설치

Pycharm 기준

File > Settings > Project Interpreter > + 버튼 > selenium 검색 후 인스톨



혹은 터미널

```
pip install selenium
```



Selenium의 버전은 자주 업데이트 되고, 브라우저의 업데이트 마다 새로운 Driver를 잡아주기 때문에 항상 최신버전을 깔아 주는 것이 좋다.



#### 크롬 웹 드라이버 설치

http://chromedriver.chromium.org/downloads



### 메뉴얼

- https://selenium-python.readthedocs.io/index.html
- https://docs.seleniumhq.org/docs/



### 웹페이지 화면을 캡쳐하여 저장

```python

from selenium import webdriver

# 1. webdriver 객체생성
driver = webdriver.Chrome('./webdriver/chromedriver.exe')
driver.implicitly_wait(3) # 3초 대기

# 2. 페이지 접근
driver.get('http://www.daum.net')

# 3. 화면을 캡처해서 저장하기
# 설치경로
driver.save_screenshot('./webdriver/WebImage.png')

driver.close()
```



### 크롬웹드라이버로 구글 검색

구글 검색창 input name 확인 !

```python
# [1]
from selenium import webdriver

# 1. webdriver 객체생성
driver = webdriver.Chrome('./webdriver/chromedriver.exe')
driver.implicitly_wait(3) # 3초 대기

# 2. 페이지 접근
driver.get('http://www.google.com')

#----------------------------------------------
# [2]
# 구글 검색창 input name : q
search = driver.find_element_by_name('q')
search.send_keys('코로나 극복')
# 폼 태그 안에 인풋 타입이 텍스트인 애가 하나만 있으면 엔터 쳤을 때 자동 서브밋
search.submit()

driver.close()
```



### 네이버 로그인

```python
"""
네이버 로그인 페이지를 실행하기
    크롬에서 네이버 로그인 페이지를 개발자모드에서 확인하여
    로그인 폼의 아이디와 비밀번호 입력 name 확인
    아이디 : id
    비밀번호 : pw
"""
import time

from selenium import webdriver

# 0. 네이버 로그인 정보
myID = '아이디'
myPW = '패스워드'

# 1. webdriver 객체생성
driver = webdriver.Chrome('./webdriver/chromedriver.exe')
driver.implicitly_wait(3) # 3초 대기

# 2. 페이지 접근
driver.get('https://nid.naver.com/nidlogin.login')

# 네이버의 경우 아래 방식이 막혀있음
# driver.find_element_by_name('id').send_keys(myID)
# driver.find_element_by_name('pw').send_keys(myPW)
# driver.find_element_by_name('log.login').click()

# 자바스크립트를 통해 전송
# 이거도 막힘..
driver.execute_script("document.getElementsByName('id')[0].value=\'" + myID + "\'")
driver.execute_script("document.getElementsByName('pw')[0].value=\'" + myPW + "\'")
driver.find_element_by_id('log.login').click()
```



## Folium

> 지도 데이터 시각화 라이브러리



### 설치 

```
pip install folium
```



```python
import folium

# 위도, 경도 지정
# 줌 설정
map = folium.Map(location=[37.24197957372821, 131.86467486531407], zoom_start=16)

# 마커
folium.Marker(location=[37.24197957372821, 131.86467486531407],
              popup="독도",
              icon=folium.Icon(color='red', icon='info-sign')).add_to(map)

# 서클 마커
folium.CircleMarker(location=[37.50376049896291, 130.85725563339628],
              popup="울릉도",
              radius=100, color='blue', fill_color='white').add_to(map)

map.save('map/map3.html')
```







## Analysis

### Tool : Jupyter 사용 권장

#### 세팅

1. 응용프로그램 우클릭
2. 속성 - 경로에 적용할 repository 추가

<hr>

### 판다스 (Pandas)

- 핵심객체는 DataFrame이다
- 데이타프레임은 2차원 데이터 구조체로 넘파이보다 편리하게 데이타 핸들링한다.
- R 언어의 데이타 프레임과 비슷하고 많이 사용된다



#### 판다스를 사용하는 이유


만일 파이썬의 리스트와 판다스의 Series가 거의 유사하다면, 우리는 왜 파이썬의 리스트가 아닌 판다스의 Series를 사용할까? 

파이썬의 리스트를 사용하면 판다스에서 제공하는 다양한 기능을 사용할 수 없기 때문이다.



[참고]

https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf

<hr>

### Series

- DataFrame의 한 컬럼 데이터 세트
- Series 역시 DataFrame의 인덱스와 동일한 인덱스를 가진다
- 즉 Series는 컬럼이 하나인 데이타 구조체이고, DataFrame은 컬럼이 여러개인 데이타 구조체이다

```python
import pandas as pd
age_in = pd.Series([22,33,44,25,28])
age_in

# 인덱스 시작번호, 끝번호, 간격
age_in.index

# 값 리스트
age_in.values
```



#### Series 인덱스

- 리스트, 튜플의 index와  dict 의 key 와 유사
- 같은 값의 index 가 가능 ( 즉, **중복 가능** )



- 리스트 튜플 index : 일련번호로 변경불가 / 순서 개념이 있다

- Series Index : 중복 가능 / 순서 개념이 있다
- Dict key : 중복 불가 / 순서 개념 없다



##### 인덱스 지정하여 시리즈 생성

```python
src = pd.Series(['가', '나', '다'], index=['a', 'b', 'a'])
print(src)

print(src['a'])
src['b'] = '안녕'
src['a'] = '헬로'
```



##### 딕셔너리를 시리즈 형태로 변환

```python
info_list = { 'kim': 25, 'park':22, 'lee':34 }

info_serise = pd.Series(info_list.values(), index=['a', 'b', 'c'])
info_serise
```





### DataFrame

#### 1. 열(컬럼) 추출

```python
df.컬럼명
df['컬럼명']
```



#### 2. 행 추출

```python
df.loc[] : 인덱스 지정하지 않으면 인덱스(순서), 인덱스 지정하면 인덱스로 추출
df.iloc[] : 인덱스(순서)로 추출
df.ix[] : 명칭 기반 인덱싱과 위치 기반 인덱싱 모두 사용 (* 그러나 곧 사라질 예정 )
```

 [참고] 

- 위 3 연산자는 노련한 개발자들도 혼동하기에, 일반적으로 하나만 선택해서 사용하는 것을 권장한다
- 넘파이와 유사한 부분으로 더우 혼동하기 쉽다
- 판다스의 DataFrame와 Series에서도 다른이 있어서 주의해야 한다



#### 3. 행과 열에서 추출

```python
df.loc[2, 3] : 2 행의 3열 데이터
df.loc[1:3, 2:4] : 1부터 3행전까지의 행에서 2부터 4전까지의 열의 데이터
```



##### 데이터 프레임 자료 생성

```python
import pandas as pd

# 데이타 프레임 자료 생성
mydata = {
          'name':['홍길동','박길동','김길동'], 
          'age':[22,33,44], 
          'dept':['컴공','국어','산업']
         }
df = pd.DataFrame(mydata)
df
```



##### dept 열(컬럼) 추출

```python
df.dept
df['dept']
```



##### 1행(레코드 추출)

```pyth
df.loc[1]
```



##### 컬럼 추가

```python
df['gender'] = ['여자','남자','여자']
```



##### 행 추가

```python
df.loc[3] = ['장길동', 55, '전자', '남자']
```



iloc 는 접근 가능할까?

```python
df.iloc[4] = ['짱길동', 55, '전자', '남자']
# 행 추가는 loc로만 가능
```



##### 변경

```python
# 인덱스순서를 변경하려면 -> 인덱스는 우선 DataFrame이 있는 상태에서 변경해야 한다
df = df.reindex(index=[0,2,5,3,1])

# 존재하지 않는 인덱스 포함 변경이 NaN 값이 들어간 데이터가 삽입됨
df = df.reindex(index=[0,1,2,3])
```



##### [중요] 컬럼 연산

> DataFrame을 쓰는 이유

```python
# 기존 존재하는 컬럼을 기준으로 연산된 컬럼 추가
# 존재하지 않는 컬럼시  '새로 추가'
# 존재하는 컬럼은 '데이터 변경'
df['age + 10'] = df['age'] + 10
```



##### 특정 행의 열값을 변경

```python
df.loc[2, 'dept'] = '산업2'
```



##### 특정 조건 레코드 검색

```python
# 30세 이상의 레코드 겁색
df[df['age'] > 30]
```



#### 데이터 필터링

- 넘파이와 유사한 부분으로 더우 혼동하기 쉽다
- 판다스의 DataFrame와 Series에서도 다른 부분이 있어서 주의해야 한다


1. loc[] : 인덱스와 명칭으로 추출

2. iloc[] : 인덱스로 추출

3. ix[] : 명칭 기반 인덱싱과 위치 기반 인덱싱 모두 사용 (*  그러나 곧 사라질 예정 )


위 3 연산자는 노련한 개발자들도 혼동하기에, 일반적으로 하나만 선택해서 사용하는 것을 권장한다



##### 명칭기반 인덱스

```python
# 행 추출
df.loc[2]

# 열 추출
df['name']

# 행 추출 (여러개)
df.loc[[2, 5, 1]]

# 열 추출 ( 여러개 : name, dept, gender )
df[['name', 'dept', 'gender']]

# 열 추출 ( 여러개 : name, dept, gender ) + 특정 행
df.loc[[2, 5, 1],['name','dept', 'gender']]
```



##### 특정 컬럼으로 인덱스 지정

```python
df.set_index('name')

df2 = df.set_index('name')

# inplace=True -> 원본 덮어쓰기
# 권장하지 않는 방법
df.set_index('name', inplace=True)
```



##### 정렬과 T

```python
# 나이를 오름차순으로
# df.sort_index(ascending=0)   # 인덱스 정렬 기본값이 ascending=1
df.sort_values('age')
df.sort_values('age', ascending=0)

df2 = df.sort_values('age', ascending=0)

# 행과 열 변경
df.T
```



##### 정보확인

```python
# 총 데이터 건수와 데이타 타입등 정보 확인
df.info()

# 기본통계량 구하기 ( 총개수, 평균, 표준편차, 최소값, 4분위수 등)
df.describe()
```



### 데이터 시각화

```python
# 데이터
data = pd.read_csv('data/president_heights.csv')

data.info() # 정보
data.mean() # 평균
data.min() # 최소값
data.max() # 최대값
data.median() # 얜 뭐냐
```

#### 1. DataFrame / Series 함수

#### 2. matplotlib 라이브러리

#### 3. seaborn 라이브러리

#### 4. 판다스 내부함수

```python
import pandas as pd

data['height'].plot(kind = 'hist')
```

