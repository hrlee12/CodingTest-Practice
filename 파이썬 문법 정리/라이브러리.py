import random

# 0~1사이의 실수값을 랜덤으로 반환 : random.random()
print(random.random())


# 정수값을 랜덤 반환하기 : random.randint(시작값, 끝값(포함))
print(random.randint(1, 10))




#실습.
li = []
while len(li) < 6:
    tmp = random.randint(1, 45)
    if tmp not in li:
        li.append(tmp)



print(li)