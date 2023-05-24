# 1차원배열_최댓값




numbers = []

for i in range(9):
    numbers.append(int(input()))

biggest = max(numbers)

idx = numbers.index(biggest)


print(biggest)
print(idx+1)
