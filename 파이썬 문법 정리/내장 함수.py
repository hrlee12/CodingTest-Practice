# 절대값 : abs()
print(abs(-2))



# 모두 참인가? all()
print(all([True, True]))
# 0은 false
print(all([1, 2, 3, 0]))


# 한개라도 참인가? any()
print(any([1,2,3, 0]))

# 아스키코드 -> 문자 : chr()
print(chr(97))
# 문자 -> 아스키코드 : ord()
print(ord('A'))

# 대상이 가지고 있는 변수나 함수 보여주기 : dir()
print(dir([1, 2, 3]))

# 실행가능한 문장을 문자열 형태로 받아 실행해줌. : eval()
print(eval('1+2'))



# filter : 조건이 참인 요소만 리스트로 반환. 
def isjjaksu(num):
    if num %2 ==0: return num

print(list(filter(isjjaksu, [1, 2, 3, 4])))

# 정수를 16진수로 변환하기 : hex()
print(hex(12))

# 정수로 변환하기 : int()
print(int(1.2))


# 최댓값 찾기 : max()
print(max([1, 2, 3]))
print(max("python"))


# 반올림하기 : round()
print(round(3.4))
print(round(3.6))







# 실습 
print(list(filter(lambda x: x>0, [1, -2, 3, -5, 8, -3])))

print(int('0xea', 16))

li = [-8, 2, 7, 5, -3, 5, 0, 1]
print(max(li))
print(min(li))

print(round(5.66666666666666, 4))