# while_A+B_5


numbers = []

while True:
    a, b = map(int, input().split())
    if a==0 and b==0: break
    numbers.append((a, b))


for a, b in numbers:
    print(a+b)
