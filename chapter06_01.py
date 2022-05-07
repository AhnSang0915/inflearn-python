# Chapter06-01
# 파이썬 클래스
# OOP(객체지향 프로그래밍), self, 인스턴스 메소드, 인스턴스 변수
# 클래스는 붕어빵 기계

# 클래스 and 인스턴스 차이 이해

# 예제1

from inspect import _Object


class Dog: # object 상속
    #클래스 속성
    species = 'firstdog'

    # 초기화/인스턴스 속성
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 클래스 정보
print(Dog)