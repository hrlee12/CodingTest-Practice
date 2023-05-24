


num = int(input())
marks = list(map(int, input().split()))
biggest = max(marks)

new_marks = []

for i in marks:
    new_marks.append(i / biggest * 100)

result = 0
for i in new_marks:
    result += i

print(result / num)
