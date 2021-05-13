"""
     1) 클래스 기초

     ` __init__ 함수 : 객체 초기화 함수( 생성자 역할 )
     ` self : 객체 자신을 가리킨다.
"""


class Sample:
    data = "헬로우"

    # 생성자
    # self.변수명 -> 멤버변수
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('__init__ 생성자 호출')

    # 소멸자
    # def __del__(self):
    #     self.name = ''
    #     self.age = 0
    #     print('__del_- 호출')


# 객체 생성
s = Sample('홍길동', 24)
# del s
print('이름 : ', s.name)
print('나이 : ', s.age)

"""
    2) 
    인스턴스 함수 :  'self'인 인스턴스를 인자로 받고 인스턴스 변수와 같이 하나의 인스턴스에만 한정된 데이터를 생성, 변경, 참조
    클래스   함수 :  'cls'인 클래스를 인자로 받고 모든 인스턴스가 공유하는 클래스 변수와 같은 데이터를 생성, 변경 또는 참조
     
    - 클래스 함수는 클래스명 접근
 
"""
print('-----------------------------')


class Book:
    cnt = 0

    def __init__(self, title):
        self.title = title

    @classmethod
    def output(self):
        # print('제목은 : ', self.title)
        self.cnt += 1
        print('총갯수 : ', self.cnt)

# 객체 생성
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

'''
     3) 클래스 상속
        - 파이션은 method overriding은 있지만 method overloading 개념은 없다
        - 파이션은 다중상속이 가능
        - 부모 클래스가 2개 이상인 경우 먼저 기술한 부모클래스에서 먼저 우선 해당 멤버를 찾음
'''
print('----------------------------')

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

class Werewolf(Wolf, Human):
    def move(self):
        # 부모의 move() 호출
        # 2개로부터 상속받았다면 앞의것을 호출한다
        super().move()
        print('늑대인간은 두발로, 네발로 모두 달릴수 있다')

# ww = Wolf()
# ww.move()
#
# h = Human()
# h.move()

w = Werewolf()
w.move()