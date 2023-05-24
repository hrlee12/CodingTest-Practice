# 1차원배열_숫자의개수


numbers = []

for i in range(3):
    numbers.append(int(input()))

number = numbers[0] * numbers[1] * numbers[2]
number = list(str(number))

for i in range(10):
    print(number.count(str(i)))
g
