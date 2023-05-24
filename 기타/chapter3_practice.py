import math
result = 0
i = 1

while i <= 1000:
    if i%3==0:  result += i
    i += 1



print(result)


i = 0

while i < 5:
    i += 1
    print('*' * i)

for i in range(1, 101):
    print(i)
    
    
a = 'hello'
b = ['a', 'b', 'c', 'd', 'e']

print(a[-1])
print('h' in a)
print('h' not in a)
print('a' in b)
print('a' not in b)


A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0
for i in A:
    total += i

print(total / len(A))

# 실수 나누기
print( 4/ 3)
# 정수 나누기
print( 4//3)


print(round(3.14))
result = []
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 1: 
        result.append(num*2)
        numbers[numbers.index(num)] = num*2


print(result)
print(numbers)

