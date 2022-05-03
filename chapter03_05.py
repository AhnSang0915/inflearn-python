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

#딕셔너리 추가
print('a - ', len(a)) # 키의 갯수 
print('a - ', len(b))
print('a - ', len(c))
print('a - ', len(d))

# dict_keys, dict_value, dict_items : 반복문(__iter__)에서 사용 가능

print('a _ ', a.keys())
print('a _ ', b.keys())
print('a _ ', c.keys())
print('a _ ', d.keys())
print('a _ ', list(a.keys()))
print('a _ ', list(b.keys()))

print()

print('a _ ', a.values())
print('a _ ', b.values())
print('a _ ', c.values())
print('a _ ', list(a.values()))
print('a _ ', list(b.values()))
