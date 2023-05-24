# 일단 모든 n x m에 대해서 이중 for문으로 탐색 함수를 돌린다. 

# 탐색 함수에서는 값이 0이면 1로 바꿀 것이고 True를 리턴할 것이다.
# 그리고 return 전에 상하좌우 노드에 대해서 재귀적으로 dfs를 호출하고 0이면 1로 바꾸고 탐색을 계속한다.
# 더이상 0으로 연결된 노드가 없을 때 가장 바깥 함수가 최종적으로 리턴이 된다. 

# 값이 0이 아니면 false를 반환한다. 


# 모든 n x m 에 대해서 탐색 함수를 실행하지만 
# 최초의 0이였던 노드도 하나의 얼음구멍으로 이미 포함되어 있다면
# 1로 값을 바꾸었기 때문에 중복해서 count를 더하는 일은 없다. 


# 재밌는 부분은 재귀함수에서 True 혹은 False를 리턴하지만 그 리턴값은 오직 가장 최초에 호출된 함수
# 즉 가장 바깥에 있는 함수가 리턴되어 함수를 완전히 빠져나올 때만 쓰인다. 
# 재귀함수에서는 더 깊게 들어가면서 0을 1로 바꾸는 기능이 수행된다. 



n, m = map(int, input().split())

graph = []
for i in range(n):
    
    # 문자열이 map의 입력값(반복 가능한 자료형)으로 들어가면 문자열의 문자 하나하나 끊어서 iteration을 돌린다. 
    # '001' -> '0', '0', '1'
    graph.append(list(map(int, input())))
    
    
print(graph)

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y>=m:     # <= 어차피 for문에서 넣어줄 인덱스는  
        return                                    #    전부 범위 내의 인덱스 이므로 return으로 수정. 
    if graph[x][y] == 0:
        graph[x][y]= 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)                             
        return True                             # <= 값이 0이면 True를 리턴
    return False                                # <= 값이 0이 아니면 False를 리턴

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1
            

print(result)