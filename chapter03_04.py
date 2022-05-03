# chapter03-04
# 파이썬 튜플
# 리스트와 비교 중요
# 튜플 자료형(순서, 중복 가능, 수정, 삭제 불가능)

# 선언

from re import T


a = ()
b = (1, ) # 콤마를 찍어야 타입이 튜플로나옴
c = (11, 12, 13, 14)
d = (100, 1000, 'Ace', 'Base', 'Captine')
e = (100, 1000, ('Ace', 'Base', 'Captine'))


# 인덱싱
print('>>>>>')
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1])
print('d - ', e[-1][1])
print('d - ', list(e[-1][1])) # 튜플e 의 -1번쨰 요소의 1번째 요소를 리스트로 만든다


# 수정 x

# 슬라이싱
print('>>>>>')
print('d - ', d[0:3])
print('d - ', d[2:])
print('d - ', e[2][1:3])

# 튜플 연산
print('>>>>>')
print('c + d', c + d)
print('c * ', c * 3)

# 튜플 함수
a= (5, 2, 3, 1, 4)
print('a - ', a)
print('a - ', a.index(3)) # 숫자 3이 들어있는 인덱스 위치
print('a - ', a.count(2))

# 팩킹 & 언팩킹(Packing, Unpacking)

# 팩킹
t = ('foo', 'bar', 'baz', 'qux')
print(t)
print(t[0])
print(t[-1])

# 언팩킹1
(x1, x2, x3, x4) = t # 괄호가 있던 없던 언패킹이 가능하지만 관례적으로 괄호로 묶어준다

print(type(x1), type(x2), type(x3), type(x4))
print(x1, x2, x3, x4)


# 팩킹 & 언팩킹
t2 = 1, 2, 3 # 괄호가 없어도 튜플
t3 = 4, # 마찬가지로 , 콤마를 붙였기 때문에 튜플
x1, x2, x3 = t2 # 언패킹
x4, x5, x6 = 4, 5, 6# 언패킹

print(t2)
print(t3)
print(x1, x2, x3)
print(x4, x5, x6)