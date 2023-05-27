def solution(N, stages):
    answer = []
    length = len(stages)
    for i in range(N):
        current = stages.count(i+1)
        if length == 0:
            answer.append((i+1, 0))
        else:
            answer.append((i+1, current/length))
        length -= current
    
    answer = sorted(answer, key=lambda data: -data[1])
    answer = [i[0] for i in answer]
    return answer
    
