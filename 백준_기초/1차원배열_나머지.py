# 1차원배열_나머지


numbers = []

for i in range(10):
    numbers.append(int(input()))


remainders = []

for i in numbers:
    remainders.append(i%42)

remainders = set(remainders)
print(len(remainders))

    
