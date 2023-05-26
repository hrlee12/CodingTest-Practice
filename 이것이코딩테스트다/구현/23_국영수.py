import sys

N = int(sys.stdin.readline())
array = []
for _ in range(N):
    tmp = sys.stdin.readline().split()
    tmp = [tmp[0]] + list(map(int, tmp[1:]))
    array.append(tmp)

idx = 0
array.sort(key=(lambda data: data[1]), reverse=True)
while idx <= N-1:
    same_idx = idx
    while True:
        if (array[same_idx][1] == array[same_idx+1][1])