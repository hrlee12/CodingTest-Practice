# 1차원배열_평균은넘겠지



num = int(input())

for i in range(num):
    numbers = list(map(int, input().split()))
    avg = 0
    num_students = numbers[0]
    for j in numbers[1:num_students+1]:
        avg += j
    avg /= num_students
    rate = 0
    for k in numbers[1:num_students+1]:
        if k > avg: rate += 1
    rate = rate / num_students * 100
    rate = round(rate, 3)
    print("%0.3f" % rate+'%')
