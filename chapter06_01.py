# Chapter06-01
# 파이썬 클래스
# OOP(객체지향 프로그래밍), self, 인스턴스 메소드, 인스턴스 변수
# 클래스는 붕어빵 기계

# 클래스 and 인스턴스 차이 이해
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 접근 가능, 공유
# 인스턴스 변수 : 객체마다 별도 존재

# 예제1

from calendar import c
from this import d
from tkinter import W


class Dog2: # object 상속
    #클래스 속성
    species = 'firstdog' # 해당클래스의 모든 인스턴스가 공유한다.

    # 초기화/인스턴스 속성
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 클래스 정보
print(Dog2)

# 인스턴스화
a = Dog2("mikky", 2)
b = Dog2("baby", 3)


# 비교

print(a==b, id(a), id(b))  # 다르다

# 네임스페이스
print('dog1', a.__dict__)
print('dog2', b.__dict__)

# 인스턴스 속성 확인
print('{} is {} and {} is {}'.format(a.name, a.age, b.name, b.age))

if a.species == 'firstdog':
    print('{0} is a {1}'.format(a.name, a.species))

print(Dog2.species)
print(a.species)
print(b.species)

# 예제2
# self의 이해
class SelfTest:
    def func1(): #클래스 메소드
        print('Func1 called')
    def func2(self): #인스턴스 메소드
        print(id(self))
        print('Func2 called')

f = SelfTest()

# print(dir(f))
print(id(f))
# f.func1() #예외
f.func2()
SelfTest.func1()
# SelfTest.func2() # 예외
SelfTest.func2(f)

# 예제3
# 클래스 변수, 인스턴스 변수
class Warehouse:
    stock_num = 0
    def __init__(self, name):
        self.name = name
        Warehouse.stock_num += 1
    def __del__(self):
        Warehouse.stock_num -= 1

user1 = Warehouse('Lee')
user2 = Warehouse('Cho')

print(Warehouse.stock_num)
# Warehouse.stock_num = 50
print(user1.name)
print(user2.name)
print(user1.__dict__)
print(user2.__dict__)
print('before', Warehouse.__dict__)
print('>>>', user1.stock_num)

del user1
print('after', Warehouse.__dict__)

# 예제4

class Dog: # object 상속
    #클래스 속성
    species = 'firstdog'

    # 초기화/인스턴스 속성
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def info(self):
        return '{} is {} years old'.format(self.name, self.age)

    def speak(self, sound):
        return '{} says {}!'.format(self.name, sound)
    
# 인스턴스 생성
c = Dog('july', 4)
d = Dog('Marry', 10)
# 메소드 호출
print(c.info())
print(d.info())
# 메소드 호출
print(c.speak('Wal Wal'))
print(d.speak('Mung Mung!'))