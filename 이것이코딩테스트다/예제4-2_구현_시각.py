import sys

num =  int(sys.stdin.readline())
count = 0
for time in range(num+1):
    for minute in range(60):
        for second in range(60):
            total_time = str(second) + str(minute) + str(time)
            if '3' in total_time: count+= 1
                
print(count)