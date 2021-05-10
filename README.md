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



#### List

- 임의의 객체를 순차적으로 저장하는 집합 자료형
- 각 값에 대해 인덱스 부여
- 변경가능 (중요)
- 대괄호 [ ] 사용

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

