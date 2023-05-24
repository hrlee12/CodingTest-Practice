import itertools
import math

# 일어날 수 있는 경우의 수가 적으므로 완전탐색
#  ( n<=200 weak<=15 dist <=8 )



# 문제 상황이 원형 : 큰수 -> 작은 수로 넘어갈 때 스무스하게 넘어가기 위해 
#                   취약점 weak는 외벽의 길이를 더한 배열을 붙여준다. 
#                    weak = weak + [w+n for w in weak]

# 커버하는 취약점의 시작점을 각각 다르게 해서
# 친구들이 커버할 수 있는 거리의 모든 조합에 해당하는 순열을 구해서 계산한다. 


def solution(n, weak, dist):
    weakSize = len(weak)
    weak = weak + [w+n for w in weak]
    minCnt = math.inf
    # 각 취약점을 시작점으로 iteration하는 for문
    for start in range(weakSize):
        # dist로 만들 수 있는 모든 순열로 for문
        # 모든 친구의 순서의 경우의 수를 때려박아 계산
        for d in itertools.permutations(dist, len(dist)):
            cnt = 1
            pos = start
            for i in range(1, weakSize):
                nextPos = start + i
                diff = weak[nextPos] - weak[pos]
                # 다음 취약점이 이 친구가 커버칠 수 있는 것보다 큰가?
                # 참이면 다음 취약점으로 넘어가고 다음 선수 내보냄 
                # 거짓이면 지금 커버치고 있는 취약점의 시작을 그대로 두고 선수도 그대로 
                if diff > d[cnt-1]:
                    pos = nextPos
                    cnt += 1
                    # 친구의 수보다 cnt가 커지면 현재 친구 순열의 한 바퀴
                    # for i in range(1, weakSize) 를 break
                    # 다음 친구의 순열로
                    if cnt > len(dist):
                        break
            if cnt <= len(dist):
                minCnt = min(minCnt, cnt)
    if minCnt == math.inf:
        return -1
    return minCnt
    
    

# def solution(n, weaks, dist):
#     max_people = len(dist)
#     len_weaks = len(weaks)
#     dist.sort(reverse=True)
    
#     # 이웃한 weak간의 간격 구하기
#     weak_dists = []
    
#     # 맨 첫번째 수와 맨 마지막 수의 간격 먼저 구하기
#     weak_dists.append(weaks[0] - weaks[-1] - n)
    
#     # 나머지 weak들의 간격 구하기
#     for idx in range(1, len_weaks):
#         tmp = weaks[idx] - weaks[idx-1]
#         weak_dists.append(tmp)
        
#     max_index = weak_dists.find(weak_dists.max()) 
#     weak_dists[max_index] = False
#     # weak_dists.pop(max_index)
#     # sums = weak_dists[max_index:] + weak_dists[:max_index]
    

#     for people_num in range(1, max_people+1):
#         min_idx = 0
#         min_sums = 0
#         global_min = 0
#         for i in range(len_weaks):
#             test_dists = weak_dists
# def solution(n, weaks, dist):
#     max_people = len(dist)
#     len_weaks = len(weaks)
#     dist.sort(reverse=True)
    
#     # 이웃한 weak간의 간격 구하기
#     weak_dists = []
    
#     # 맨 첫번째 수와 맨 마지막 수의 간격 먼저 구하기
#     weak_dists.append(weaks[0] - weaks[-1] - n)
    
#     # 나머지 weak들의 간격 구하기
#     for idx in range(1, len_weaks):
#         tmp = weaks[idx] - weaks[idx-1]
#         weak_dists.append(tmp)
        
#     max_index = weak_dists.index(max(weak_dists)) 
#     weak_dists[max_index] = False

    

#     for people_num in range(1, max_people+1):
#         min_idx = 0
#         min_sums = 0
#         global_min = 0
#         for i in range(len_weaks):
#             test_dists = weak_dists
#             test_dists[i] = False
#             print(test_dists)
#             last_False_idx = 0
#             for j in range(len_weaks):
#                 if test_dists[j] == False: last_False_idx = i

#             idx = last_False_idx
#             sums = [0]
#             sums_idx = 0
#             while True:
#                 last_index = len_weaks-1
                
#                 # 다음 인덱스로 넘어가기 
#                 # 연결리스트 구현
#                 if idx == last_index: idx = 0
#                 else: idx +=1

#                 # 끊는 부분에서 그만 더하고 새로운 뭉탱이 더하기 
#                 # -> False를 만났을 때, sums_idx 를 하나 올리기
#                 if not test_dists[idx]: 
#                     sums.append(0)
#                     sums_idx += 1
                
#                 # 외벽 전체를 다 수리했을 때 끝내기
#                 # -> iteration을 다 돌았을 때, 반복문을 끝내기
#                 if idx == last_False_idx: break
                
#                 # 뭉탱이 더하기
#                 sums[sums_idx] += test_dists[idx]
#                 print(sums)
#             print(sums)
#             max_one = 0
#             for i in sums:
#                 if i > max_one : max_one = i
            
#             if max_one < global_min:
#                 global_min = max_one
#                 min_idx = i
#                 min_sums = sums
#             print(min_sums)
#         weak_dists[min_idx] = False
#         min_sums.sort(reverse=True)
                
#         is_enough = True
        
        
#         print('dist >> ',  dist,  'min_sums >> ', min_sums)

#         for i in range(people_num):
#             if dist[i] < min_sums[i]: is_enough = False
#             print('dist[i] >> ',  dist[i],  'min_sums[i] >> ', min_sums[i])
        
#         if is_enough: return people_num

        
    
#     return -1

# n = 12	
# weaks = [1, 5, 6, 10]	
# dist = [1, 2, 3, 4]
# print(solution(n, weaks, dist))



