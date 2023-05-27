

def solution(N, stages):
		# 현재 스테이지에 있는 플레이어 초기화
		# 스테이지는 1부터 시작하므로 0을 안 쓰고 1 ~ N+1의 인덱스를 사용 
    on_stage = [0] * (N+2)
		# 스테이지를 거친 플레이어 초기화 
    start_stage = [0] * (N+1)
		
		# 스테이지에 현재 있는 플레이어 계산
		# 스테이지에 해당하는 인덱스의 값을 올려줌. 
    for i in range(0, len(stages)):
        on_stage[stages[i]] += 1
    
		# 스테이지를 거친 플레이어 계산
		# 스테이지 5에 있는 플레이어는 스테이지 1을 거침. 
		# -> 마지막 스테이지부터 계산. 
		# ex) 스테이지2 거친 사람 수는 스테이지3 거친 사람 수 + 현재 스테이지 2에 있는 사람 수
    for i in range(N, 0, -1):
        if i == N :
            start_stage[i] = on_stage[N+1] + on_stage[i]
        else:
            start_stage[i] = start_stage[i+1] + on_stage[i]
    
		# 실패율 계산
    failure_rate = []
    for i in range(1, len(start_stage)):
        if start_stage[i] == 0:
            failure_rate.append((i, 0))
        else:
            failure_rate.append((i, on_stage[i]/start_stage[i]))
    
		# 정렬
    result = sorted(failure_rate, key=lambda data: (-data[1], data[0]))    
    for i in range(len(result)):
        result[i] = result[i][0]
    return result


print(solution(4, [4, 4, 4, 4, 4]))

