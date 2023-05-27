from collections import deque
import sys

# 인접리스트 만드는 함수
# 입력값 : 이차원 배열
def getAdj(matrix, len, min, max) :
 adj = [[[]for _ in range(len)] for _ in range(len)]
 print(adj)
 dx = [0, 0, -1, 1]
 dy = [1, -1, 0, 0]
 for x in range(len):
     for y in range(len):
        for k in range(4):
            if (x+dx[k] < 0 or x+dx[k] >= len or y+dy[k] < 0 or y+dy[k] >= len):
                continue
            tmp = abs(matrix[x][y] - matrix[x+dx[k]][y+dy[k]])
            if (tmp >= min and tmp <=max):
                adj[x][y].append([x+dx[k], y+dy[k]])
 return adj
     

def bfs(adj, visited, x, y):
       queue = deque()
       queue.append([x, y])
       
       while queue: 
           target = queue.popleft()
           for adj_x, adj_y in (adj[target[0]][target[1]]):
               if visited[adj_x][adj_y] == 0:
                   visited[adj_x][adj_y] = 1
                   queue.append([adj_x, adj_y])
       

L, N, R = map(int, sys.stdin.readline().split())
matrix = []
for i in range(L):
    matrix.append(list(map(int, sys.stdin.readline().split())))
print(matrix)
count = 0
while True:
    adj = getAdj(matrix, L, N, R)
    check = False
    for i in range(N):
        for j in range(N):
            if getAdj[i][j]:
                check = True
    if not check : break
    for i in range(N):
        for j in range(N):
            if 
            
# adj = getAdj([[50, 30], [20, 40]], 2, 20, 50)
# print(adj)  
