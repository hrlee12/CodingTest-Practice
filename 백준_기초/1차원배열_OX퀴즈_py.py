# 1차원배열_OX퀴즈_py


num = int(input())
marks = []

for i in range(num):
    marks.append(input())


result = []

for i in marks:
    sum = 0
    mark = 0
    for j in i:
        if j == 'O': mark += 1
        else: mark = 0
        sum += mark
    result.append(sum)

for i in result:
    print(i)

