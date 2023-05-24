def solution(n, m, section):
    if m == 1: return len(section)
    count = 0
    gap = 1
    justPainted = False
    for i in range(len(section)-1):
        if justPainted: 
            justPainted = False
            continue
        gap += section[i+1] - section[i]
        if (gap >= m): 
            count += 1
            gap = 1
            if (gap == m): 
                justPainted = True
    
    if not justPainted:  count+= 1            
    
    return count


result = solution(8, 4, [2, 3, 6])
print(result)

[1, 2, 3, 6,7]

마지막에 : 
    딱 맞는경우 - 그냥 둠
    부족한 경우 - 하나 더해줌
    남는 경우  - 하나 더해줌. 


1) 갭을 더해가다가 롤러의 폭이 되면 카운트 되고 갭은 초기화. 
2) 갭을 더하는데 아예 롤러의 폭이 넘으면 이번 벽 전까지 해서 갭 1 카운트
3) 축적된 건 없는데 아예 갭이 넘어버리면 새로운 갭으로 시작. 마지막 애거나 마지막은 아닌데 또 뒤에 갭이 넘어버린다. 1 카운트
4) 롤러 폭이 3인데 2로 끝낸다. 1 카운트

1, 8, 10, 13    : 1 + 2 + 3
갭 + 1 까지 한번에 커버가 된다. 
롤러 폭보다 작으면 한번에 커버가 됨. 
갭을 여러개 더했을 때도. 
그러니까 갭을 계속 더해가다가 롤러의 폭을 넘으면 1을 카운트
또 아예 롤러의 폭을 넘으면 그건 그냥 1이야. 
1, 2, 3, 4, 5, 6, 7, 8
8, 4, [1, 3, 4, 8]