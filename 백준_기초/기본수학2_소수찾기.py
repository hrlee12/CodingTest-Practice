# 기본수학2_소수찾기



num = int(input())

numbers = map(int, input().split())

for i in numbers:
    if i == 1:
        num -= 1
    elif i == 2:
        pass
    else:
        for j in range(2, i):
           if i/j == int(i/j):
               num -= 1
               break
            

print(num)
