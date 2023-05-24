# 문자열_반복

num = int(input())

for i in range(num):
    data = input().split()
    r = int(data[0])
    for j in data[1]:
        print(j*r, end='')
    print()
    

