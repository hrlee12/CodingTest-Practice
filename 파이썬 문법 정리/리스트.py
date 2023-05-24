# 리스트는 문자열과 달리 수정 가능해서 리스트 내부 함수를 사용하면 본인을 수정한다. 


# 리스트로 형변환하기 
# 문자열은 반복가능하므로 간단히 list()로 한글자 한글자 떼서 배열로 만들 수 있음.
print('# 리스트로 형변환하기')
print(list('hello'))
print(list(set([1, 2, 3])))


# 리스트에서 요소 삭제하기 : del, remove
# 둘의 차이는 del은 인덱스를 입력해 지우고
# remove는 값을 입력해 지운다 
# del a[idx]
# a.remove(값)
print('리스트에서 요소 삭제하기 : del, remove')
a = [1, 2, 3, 4, 5, 6]
del a[0]
print(a)
del a[2:4]
print(a)

a = [1, 2, 3, 4]
a.remove(2)
print(a)




# 리스트 맨 마지막에 요소 추가  : append
print('# 리스트 맨 마지막에 요소 추가 : append')
a = [1, 2, 3]
a.append(4)
print(a)


# 리스트 정렬 : sort
# 숫자뿐만 아니라 알파벳도 정렬 가능
print('# 리스트 정렬 : sort')

a = [1, 0, -1, 4, 3, 2]
b = ['b', 'c', 'a']
a.sort()
b.sort()
print(a)
print(b)

 

# 리스트 뒤집기 : reverse
# 리스트 요소의 순서를 거꾸로 뒤집는다. 
print('# 리스트 뒤집기 : reverse')
a.reverse()
print(a)


# 여기서부터는 본인을 마꾸고 자시고 할 함수들이 아니기 때문에 결괏값을 반환한다. 
# 위치 반환 : index
# 찾는 요소가 없으면 오류 발생 (문자열의 경우와 같음. )
# 문자열과 달리 find가 없음. 
print('# 위치 반환 : index')
print(a.index(3))
# print(a.index(6))


# 리스트에 요소 삽입 : insert
# 특정 인덱스에 요소를 삽입한다. 
print('# 리스트에 요소 삽입 : insert')
a = [1, 2, 3]
a.insert(1, 4)
print(a)


# 맨 마지막 요소 꺼내기 : pop
# 맨 마지막 요소를 꺼내서 반환한다. 
print('# 맨 마지막 요소 꺼내기 : pop')
print(a.pop())
print(a)
print(a.pop(1))

 # 요소 x의 개수 세기 : count
a = [1, 1, 3, 4]
print(a.count(1))
print(a.count(2))


# 리스트끼리 붙여버리기 : extend
# javascript의 concat과 같음. 
a = [1, 2, 3]
a.extend([4, 5])
print(a)


