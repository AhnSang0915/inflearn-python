# Chapter03-05
# 파이썬 딕셔너리
# 범용적으로 가장 많이 사용
# 딕셔너리 자료형(순서x, 키 중복x, 수정o, 삭제o)

# 선언
a = {'name' : 'Kim', 'phone' : '01033337777', 'birth' : 870514}
b = {0 : 'Hello Python'}
c = {'arr' : [1, 2, 3, 4]}
d = {
    'name' : 'Niceman',
    'City' : 'Seoul',
    'Age' : 33,
    'Grade' : 'A',
    'Status' : True
}
e = dict([
    ('name' , 'Niceman'),
    ('City' , 'Seoul'),
    ('Age' , 33),
    ('Grade' , 'A'),
    ('Status' , True)
])

f = dict(
    Name = 'Niceman',
    City = 'Seoul',
    Age = 33,
    Grade = 'A',
    Status = True
)

print('a - ',type(a), a)
print('b - ',type(b), b)
print('c - ',type(c), c)
print('d - ',type(d), d)
print('e - ',type(e), e)
print('f - ',type(f), f)

# 출력
print('a - ', a['name'])
print('a - ', a.get('name')) # 키가 없는경우 None 이 나오고 에러가 나지 않기 때문에 많이 사용
print('b - ', b[0])
print('b - ', b.get(0))
print('f - ', f.get('City'))
print('f - ', f.get('Age'))

# 딕셔너리 추가
a['address'] = 'Seoul'
print('a - ', a)
a['rank'] = [1, 2, 3]
print('a - ', a)

#딕셔너리 길이
print('a - ', len(a)) # 키의 갯수 
print('a - ', len(b))
print('a - ', len(c))
print('a - ', len(d))

# dict_keys, dict_value, dict_items : 반복문(__iter__)에서 사용 가능

print('a _ ', a.keys())
print('b _ ', b.keys())
print('c _ ', c.keys())
print('d _ ', d.keys())
print('e _ ', list(a.keys()))
print('f _ ', list(b.keys()))

print()

print('a _ ', a.values())
print('b _ ', b.values())
print('c _ ', c.values())
print('a _ ', list(a.values()))
print('b _ ', list(b.values()))

print()

print('a _ ', a.items()) # 튜플 형태로 키와 밸류 출력
print('b _ ', b.items())
print('c _ ', c.items())

print('a _ ', list(a.items()))
print('b _ ', list(b.items()))

print()

print('a - ', a.pop('name')) # 꺼내오고 제거
print('a - ', a)

print('c - ', c.pop('arr')) # 꺼내오고 제거
print('c - ', c)

print()

print('f - ', f.popitem()) #임의의 키와 밸류를 꺼내고 제거
print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)

print()

print('a - ', 'birth' in a)
print('a - ', 'City' in d)

# 수정 & 추가
a['test'] = 'test_dict'

print('a - ', a)

a['address'] = 'dj'
print('a - ', a)

a.update(birth = '910904')
print('a - ', a)

temp = {'address' : 'Busan'}
a.update(temp)
print('a - ', a)