# 문자열_숫자의합



num = int(input())
numbers = map(int, input())

result = 0

for i in numbers:
    result += i

print(result)
