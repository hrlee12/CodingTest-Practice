# for_A+B


number = int(input())
result = []
for i in range(number):
    a, b = map(int, input().split())
    result.append(a+b)

for i in result:
    print(i)
