# 문자열 관련 함수

# 문자열은 수정 불가능하다. 
# 본인을 수정해서 저장해주는 애는 없고 전부 다 결과값을 반환해줌. 

# 문자열은 반복가능하다. 
a = 'Life is too short'

for i in a:
    print(i)



# 문자 개수 새기 : count
print(a.count('i'))

# 위치 알려주기 : find
# 없으면 -1 반환
print(a.find('b'))
print(a.find('o'))

# 위치 알려주기 : index
# 없으면 오류 발생
# 있는지 없는지 확인해야하는 경우는 find를 쓰자. 아니면 in
print(a.index('o'))
# print(a.index('b'))

# 있는지 없는지, 있는 경우 인덱스를 알고 싶으면 find로 가자 
print('b' in a)

# 문자열 삽입
# 헷갈리지 말자. 문자열 내부 메소드다. 
# 인자로 들어온 반복 가능한 자료형(문자열 또는 배열 등) 사이사이에 자신을 넣은 새로운 문자열을 반환한다. 
print(','.join('abcd'))
print('.'.join(['a', 'b', 'c']))


# 대소문자 반환
print(a.upper())
print(a.lower())

# 공백 지우기
# javascript에서는 trim이었는데 파이썬은 strip
a = ' hi '
print(a.strip())
print(a.lstrip())
print(a.rstrip())
# 공백으로만 이룰어진 문자는 공백 다 지우고 빈 문자열로 만들어줌. 
b = '\n   '
print(len(b.strip()))
print(len(b.lstrip()))


# 문자열 바꾸기
a = 'Life is too short'
print(a.replace('Life', 'Your leg'))

# 문자열 나누기
# 인자로 들어온 문자를 기준으로 문자열을 나눠 배열로 반환함. 
# split에 인자가 없으면 공백을 기준으로 나눔. 
print(a.split())

#  + 연산자는 문자열 뿐만 아니라 튶플, 배열, 딕셔너리 등 
# 같은 자료형끼리 +를 하면 자료형은 그대로 유지하면서 요소를 넣어서 늘려준다. 
a = (1, 2, 3)
a = a + (4, )
# print(a)

list = [1, 2, 3, 4] + [5, 6, 7, 8]
# print(list)


a = {'A': 90, 'B':80, 'C':70}
result = a['B']
# print(result)

a = [1,1, 1, 2, 2, 3, 4, 4]
a = set(a)
# print(a)
# for i in a:
    # print(i)





a = b = [1, 2, 3]
a[1] = 4
# print(b)

# print(f'안녕하세요 {a[1]}')


a = 'python '
b = 'hello'
# print(b+ ' '+ a)
# print(a*2)

a = "Life is too short"
# print(len(a))
# print(a[0])
a = "Pithon"
a = a[0] + 'y' + a[2:]
# print(a)
