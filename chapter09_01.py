# Chapter09-01
# 파일 읽기 및 쓰기

# 읽기 모드 : r, 쓰기모드 ㅈ, 추가모드 a, 텍스트 모드 t, 바이너리 모드 b
# 상대 경로('../,./'), 절대 경로('c:\Django\example..')

# 파일 읽기(Read)
# 예제1

f = open('./resource/it_news.txt', 'rt', encoding='UTF-8')
# 속성 확인
print(dir(f))
# 인코딩 확인
print(f.encoding)
# 파일 이름
print(f.name)
# 모드 확인
print(f.mode)
cts = f.read()
print(cts)
# 반드시 close
f.close()

# 예제2
with open('./resource/it_news.txt', 'rt', encoding='UTF-8') as f:
    c = f.read()
    print(c)
    print(iter(c))
    print(list(c))
    
print()

# 예제3
# read() : 전체 읽기, read(10) : 10Byte ()안의 바이트 수만큼 읽어온다

with open('./resource/it_news.txt', 'rt', encoding='UTF-8') as f:
    c = f.read(20) # 20글자만 나온다.(20Byte)
    print(c)
    c = f.read(20)
    print(c) # 앞에 출력한 문자 다음부터 읽어오고 이말은 커서가 있다는 말이다.
             # 커서가 내부적으로 동작해 내가 마지막으로 읽은곳이 어딘지 알고있다.
    f.seek(0,0) # 처음으로 돌아간다
    c = f.read(20)
    print(c)
    
print()

# 예제4
# readline : 한 줄 씩 읽기

with open('./resource/it_news.txt', 'rt', encoding='UTF-8') as f:
    line = f.readline()
    print(line)
    line = f.readline()
    print(line)    
print()

# 예제5
# readlines : 전체를 읽은 후 라인 단위 리스트로 저장

with open('./resource/it_news.txt', 'rt', encoding='UTF-8') as f:
    cts = f.readlines()
    print(cts)
    print()
    for c in cts:
        print(c, end = '')
print()

# 파일 쓰기(write)

# 예제1
with open('./resource/comtents1.txt', 'wt') as f:
    f. write('I love python\n')

# 예제2
with open('./resource/comtents1.txt', 'at') as f:
    f. write('I love python2\n')

# 예제3
# writelines : 리스트 -> 파일
with open('./resource/comtents2.txt', 'w') as f:
    list = ['Orange\n', 'Apple\n', 'Banana\n', 'Melon\n']
    f.writelines(list)

# 예제4
with open('./resource/comtents3.txt', 'w') as f:
    print('Test Text Write!', file = f)
    print('Test Text Write!', file = f)
    print('Test Text Write!', file = f)