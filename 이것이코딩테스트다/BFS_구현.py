from collections import deque

# BFS 메서드 정의
def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위한 deque 라이브러리 사용 
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    
    # 큐가 빌 때까지 반복
    while queue: 
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    
    



# 그래프를 인접 리스트로 표현
# 인접 리스트 = 이차원 배열. 배열의 각 요소는 노드에 인접한 노드로 이루어진 배열임. 
# 노드는 1~8 여덟개지만 graph의 인덱스 = 노드 번호로 대입하므로 인덱스 0번은 빈 리스트. 
graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]

# 노드는 1~8 여덟개지만 visited의 인덱스 = 노드 번호로 대입하므로 인덱스 0번을 고려해서 원소를 9개
visited = [False]*9

bfs(graph, 1, visited)