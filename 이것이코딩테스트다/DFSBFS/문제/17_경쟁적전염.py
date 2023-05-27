from collections import deque
import sys

# 테이블의 칸이 노드이고 인접 노드는 상하좌우의 노드. 
# -> 따로 인접 리스트가 필요하지 않음.

# 이미 들른 노드에는 값이 0이 아님 -> 테이블로 visited 대체. 

# 1초 후에는 각 바이러스가 상하좌우로 한칸씩 전염.
# 1초에 각 바이러스에 대해서 dfs를 한 깊이씩 진행. -> dfs함수는 한 깊이에 대해서 진행하고 방금 새로 넣은 노드가 담긴 queue 반환. 
# 전염되는 부분이 겹치면 숫자가 작은 바이러스 우선 -> 숫자가 작은 바이러스부터 큰 바이러스 순으로 dfs진행. 

# 주어진 초만큼 반복. 

def dfs(vector, target, queue):
    # 큐에 빈 배열이 들어왔다면 -> 이 바이러스에서 최초의 dfs임. 
    # 이 바이러스가 위치한 좌표 넣어주기
    if (not queue) :
        queue = deque()
        # 좌표를 큐에 넣어줌. 
        target_index = 0
        for i in vector:
            if target in i:
                # 바이러스의 행, 열 좌표 넣어줌. 
                target_index = [vector.index(i), i.index(target)]
                # print('타켓 인덱스', target_index)
                break
        queue.append(target_index)
    
    # 인접한 노드=상하좌우 좌표 
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    
    # dfs를 한번에 전부 진행하지 않음. 
    # 현재의 깊이에 대해서만 진행하므로 새로 append되는 노드는 다른 큐에 넣어서 다음에 이어서 탐색할 수 있도록 반환해줌. 
    next_queue = deque()
    while queue:
        v = queue.popleft()
        # print(v)
    
        for i in range(4):
            x = v[0]+dx[i]
            y = v[1]+dy[i]
            if x < 0 or x >= len(vector) or y < 0 or y >= len(vector):
                continue
            # print(x,y)

            if vector[x][y] == 0:
                vector[x][y] = target
                next_queue.append([x, y])
    return (vector, next_queue)



# 입려값 받기 : 테이블 크기, 바이러스 숫자
width, virus_num = map(int, sys.stdin.readline().split())

# 입력값 받아서 배열에 넣어주기 : 분포현황(?)
vector = []
for i in range(width):
    vector.append(list(map(int, sys.stdin.readline().split())))
 
# 입력값 받기 : 초, 알고 싶은 좌표 
count, x, y = (map(int, sys.stdin.readline().split()))

# 다음에 dfs를 진행할 queue를 담는 변수 : 모든 바이러스에 대한 큐를 배열로 가지고 있음. 
queue = [[] for _ in range(virus_num)]

# count만큼 iteration
for j in range(count):
    # 각 virus에 대해서 iteration
    for i in range(virus_num):
        # 현재 테이블, 몇번째 바이러스인지, dfs를 진행할 queue (이 바이러스가 저버네 진행한 dfs에서 append된 노드 담김)
        vector, tmp = dfs(vector, i+1, queue[i])
        # print(f'{j+1}번째 {i+1} vector')
        # print(vector)
        queue[i] = tmp
 
# count초 후, 알고자 하는 노드의 번호 프린트        
print(vector[x-1][y-1])