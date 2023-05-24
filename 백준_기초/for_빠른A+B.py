# 빠른 A+B

import sys

num = int(input())
result = []
for i in range(num):
    a, b = map(int, sys.stdin.readline().split())
    result.append(a+b)

for i in result:
    print(i)
