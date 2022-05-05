# Chapter04-02
# 파이썬 반복문
# for 실습

# 코딩의 핵심
# for in <collection>
#       <loop body>


from re import L


for v1 in range(10):
    print('v1 is : ', v1)

print()

for v2 in range(1, 11):
    print('v2 is : ', v2)

print()

for v3 in range(1, 11, 2):
    print('v3 : ', v3)


# 1 ~ 1000합

sum1 = 0

for v in range(1, 1001):
    sum1 += v

print('1 ~ 1000 sum : ', sum1)

print('1 ~ 1000 sum : ', sum(range(1,1001)))
print('1 ~ 1000 4의 배수의 합 : ', sum(range(4,1001,4)))

print(type(range(1,11)))

# Iterables 자료형 반복
# 문자열, 리스트, 튜플, 집합, 딕셔너리
# iterable 리턴 함수 : range, reversed, enumerate, filter, map, zip

# 예제1
names = ['Kim', 'Park', 'Cho', 'Lee', 'Choi', 'Yoo']

for i in names:
    print('You are : ', i)

# 예제2

lotto_numbers = [11, 19, 21, 28, 26, 37]

for i in lotto_numbers:
    print("Current number : ", i)


# 예제3
word = "Beautiful"

for s in word:
    print('Word : ', s)

# 예제4
my_info = {
    "name" : "Lee",
    "Age" : 33,
    "City" : "Seoul"
}

for key in my_info:
    print('key : ', my_info[key])

for v in my_info.values():
    print('value : ', v)


# 예제5
name = 'FineAppLE'

for n in name:
    if n.isupper():
        print(n)
    else:
        print(n.upper())


# break

numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers:
    if num == 4:
        print('Found : 4!')
        break
    else:
        print('Not found : ', num)

# continue

lt = ["1", 2, 5, True, 4.3, complex(4)]

for v in lt:
    if type(v) is bool:
        continue
    print('Current type : ', v, type(v)) 

# for else

numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers:
    if num == 55:
        print("Found : 55")
        break
else:
    print('Not found : 55')

# 구구단 출력

for i in range(2,10):
    for j in range(1,10):
        print('{:4d}'.format(i*j), end = '')
    print()


# 변환 예제

name2 = 'Aceman'

print('Reversed', reversed(name2)) # 형변환을 해줘야 값을 확인할 수 있다.

print('List', list(reversed(name2)))

print('Tuple', tuple(reversed(name2)))

print('Set', set(reversed(name2))) # 집합은 순서가 없음