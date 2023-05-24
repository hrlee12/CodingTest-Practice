# 기본수학1_ACM호텔

"""
입력 : 테스트 데이터 t, 층, 방수, 손님의 도착순서
기능 : 
출력 : 손님이 배정될 방의 번호



이차원 리스트.
1차원 : i+1호대
"""

num = int(input())
data = []
for i in range(num):
    h, w, n = map(int, input().split())
    data.append([h, w, n])

for h, w, n in data:
    room = []
    for i in range(1, h+1):
        room.append(i*100 + 1)
    room_sample = room.copy()
    for j in range(1, w):
        room.extend([k + j for k in room_sample])
    print(room[n-1])
