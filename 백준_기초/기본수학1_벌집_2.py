# 기본수학1_벌집_2

"""

입력 : 방 번호
기능 : 중앙 1번방에서 주어진 번호의 방까지 최소 몇개의 방을 지나야 하는가
        -> 주어진 번호는 몇 레이어의 방인가?
출력 : 주어진 방번호가 몇 레이어에 있는가?





1 : 1 = 1 + 0 * 6
2 : 7 = 1 + 1 * 6
3 : 19 = 7 + 2 * 6
4 : 37 = 19 + 3 * 6
5 : 61 = 37 + 4 * 6
...


등열의 합

"""


room = int(input())
layer = 1
last_room = 1

if room == last_room:
    pass
else:
    while True:
        layer += 1
        last_room += (layer-1) * 6
        if room <= last_room: break

print(layer)

