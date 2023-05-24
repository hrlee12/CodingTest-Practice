# 오븐시계.py

hour, minute = map(int, input().split())
time = int(input())

tmp_minute = minute + time
hour += tmp_minute // 60
hour %= 24
minute = tmp_minute % 60

    
print("%d %d" % (hour, minute)) 
