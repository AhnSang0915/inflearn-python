# Chapter07-01
# 파이썬 예외처리의 이해
# 예외 종류
# SyntaxError, TypeError, NameError, IndexError, ValueError, KeyError...
# 문법적으로는 예외가 없지만, 코드 실행 프로세스(단계)발생하는 예외도 중요
# 1. 예외는 반드시 처리
# 2. 로그는 반드시 남긴다.
# 3. 예외는 던져진다.
# 4. 예외 무시

# SyntaxError : 문법 오류
# print('error)
# print('error'))
# if True (:을안붙였을떄)

# NameError : 참조 없음
# a = 10
# b = 15
# print(c)

# ZeroDivisionError 

# print(100 / 0)

# IndexError

# x = [50, 70, 90]
# print(x[1])
# print(x[4])

# 또는 x.pop()으로 요소를 다꺼낸후 다시 pop을 했을때

# KeyError

# dic = {'name' : 'Lee', 'Age' : 41, 'City' : 'Busan0'}
# print(dic['hobby]) # 없는 키를 가져오라고 했기 때문에 에러가 나온다
# print(dic.get('hobby')) # get을 쓰면 없으면 None을 가져오기 때문에 에러가 나오지 않는다

# 예외 없는 것을 가정하고 프로그램 작성 -> 런타임 예외 발생 시 예외 처리 권장(EAPA)

# AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용 예외\
# import time
# print(time.time2())  # 파이썬 time 모듈에 time2가 존재하지 않는다.

# ValueError

# x = [10, 50, 90]
# x.remove(50)
# print(x)
# x.remove(200) # 없는값

# FileNotFoundError

# f = open('test.txt') # 없는 파일을 열라고 했다.

# TypeError : 자료형에 맞지 않는 연산을 수행할 경우
x = [1,2] # 가변
y = (1,2) # 불변
z = 'test'

# print(x + y) # 합칠수가 없다 형이 다르기 때문에
# print(x + z) # 문자열과 리스트는 합칠 수 없다
# print(y + z) # 문자열과 튜플은 합칠 수 없다

# 형변환을 해서 합칠 수 있다.

# print(x + list(y))
# print(x + list(z))

# 예외 처리 기본
# try : 에러가 발생 할 가능성이 있는 코드를 try로 실행
# except 에러명1: 여러개 가능
# except 에러명2:
# else : try 블록의 에러가 없을 경우 실행
# finally : 항상 마지막 실행

name = ['Kim', 'Lee', 'Park']

# 예제1
# try:
#     z = 'Kim' # 'Cho'
#     x = name.index(z)
#     print('{} Found it! {} in name'.format(z, x + 1))
# except ValueError:
#     print('Not found it! - Occurred ValueError!')
# else:
#     print('Ok! else.')

# print()

# 예제2

# try:
#     z = 'Cho'
#     x = name.index(z)
#     print('{} Found it! {} in name'.format(z, x + 1))
# except Exception: # 특정 예외를 지정하지 않고 모든 에러를 지칭한다
#     print('Not found it! - Occurred ValueError!')
# else:
#     print('Ok! else.')

# print()

# 예제3

# try:
#     z = 'Cho'
#     x = name.index(z)
#     print('{} Found it! {} in name'.format(z, x + 1))
# except ValueError as e: # 특정 예외를 지정하지 않고 모든 에러를 지칭한다
#     print(e)
#     print('Not found it! - Occurred ValueError!')
# else:
#     print('Ok! else.')
# finally:
#     print('Ok! finally!')

# print()

# 예제4
# 예외 발생 : raise
# 파이썬에 원칙에 입각한 예외는 아니지만 사용자가 필요에의해 정한 예외를 발생시킬 수 있다.
# raise 키워드로 예외 직접 발생

try:
    a = 'Park'
    if a == 'Kim':
        print('OK! Pass!')
    else:
        raise ValueError # Kim이 아니면 ValueError 발생
    
except ValueError:
    print('Occured! Exception!')
else:
    print('Ok! else!')

