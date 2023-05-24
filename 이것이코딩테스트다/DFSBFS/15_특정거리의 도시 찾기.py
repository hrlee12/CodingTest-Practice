from collections import deque
import sys

# 개념 설명에서 나온 구현하는 코드랑 거의 비슷함. 
# 모든 노드를 탐색하는 것에서 나아가 탐색하면서 최단거리 체크

def dfs(start, dist, adj, visited):
    result = []
    count = 1
    queue = deque([start])
    while queue:
        v = queue.popleft()
        
        # 인접한 모든 노드에 대해서 
        for i in adj[v]:
            # 방문하지 않았다면 
            if visited[i] == -1:
                # 현재 pop한 노드의 visited값에서 1을 더한 값을 저장해줌. (몇개를 거쳤는지 표시)
                # ex) 첫번째 노드에 인접한 노드2 는 0+1 -> 1저장.    노드2가 pop되었을 때 노드2에 인접한 노드3은 1+1-> 2저장. 
                visited[i] = visited[v] + 1     
                queue.append(i)
                
    # 원하는 최단거리의 노드가 있는지 체크            
    check = False
    
    # 원하는 최단거리의 노드 출력. 
    # 올림차순으로 출력. 
    for i in range(1, len(visited)):
        if visited[i] == dist:
            print(i)
            check = True
            
    if check==False:
        print(-1)
    
    return
        

n_city, n_road, dist, start = map(int, sys.stdin.readline().split())
adj = [[] for i in range(n_city+1)]

for i in range(n_road):
    n, m = map(int, sys.stdin.readline().split())
    adj[n].append(m)

visited = [-1 for i in range(n_city+1)]
visited[start] = 0
dfs(start, dist, adj, visited)