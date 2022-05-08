# 모듈 사용 실습

import sys

print(sys.path)

print(type(sys.path))


# 모듈 경로 삽입
# sys.path.append('c:/math') # 영구적이지 않고 이 코드에서만 사용

# print(sys.path)

# import test_module

# # 모듈 사용
# print(test_module.pow(10, 3))
# print(test_module.mul(10,50))

import chapter06_02

print(chapter06_02.add(10, 10000))