# 기둥을 설치할 수 있는 조건
# 기둥이 바닥 위에 있는 경우 : 좌표가 (x, 0)
# 보의 한쪽 끝부분에 있는 경우 : 보의 좌표에서 (x+1, y) 또는 (x, y)
# 다른 기둥 위에 있는 경우 : 기둥의 좌표에서 (x, y+1)

# 보를 설치할 수 있는 조건
# 한쪽 끝부분이 기둥 위에 있는 경우 : 기둥의 좌표에서 (x, y+1) 또는 (x-1, y+1)
# 양쪽 끝부분이 다른 보와 동시에 연결되어 있는 경우 : 두개의 보의 좌표에서 각각 (x+1, y), (x-1, y)
def solution(n, build_frame):
    answer = []

    # 특정 구조물이 조건을 충족하는 지 확인하는 함수
    # 설치/철거 조건은 빼고 매개변수로 들어감. 
    def isOk(i):
        
        if i[2] == 0:
        # 기둥이 바닥 위에 있는 경우
            if i[1] == 0:
                return True        
            for j in answer:
                # 보의 한쪽 끝부분에 있는 경우 
                # 보와 y좌표가 같을 때 
                if j[2] == 1 and j[1] == i[1]:
                    # 보와의 x좌표 기준도 충족할 때
                    if j[0] == i[0]-1 or j[0] == i[0]:
                        return True
                # 다른 기둥 위에 있는 경우 : (x, y+1)
                if j[2] == 0 and j[0] == i[0] and j[1] == i[1]-1:
                    return True

        # 보일 때   
        elif i[2] == 1:
            # 한쪽 끝부분이 기둥 위에 있는 경우 : 새로운 보의 기준에서 (x, y+1) 또는 (x-1, y+1)
            if [i[0], i[1]-1, 0] in answer or [i[0]+1, i[1]-1, 0] in answer:
                return True
            # 양쪽 끝부분이 다른 보와 동시에 연결되어 있는 경우 : 새로운 보의 기준에서 좌표에서 각각 (x+1, y), (x-1, y)
            elif [i[0]+1, i[1], 1] in answer and [i[0]-1, i[1], 1] in answer:
                return True
        
        # 조건이 충족되지 않을 때
        return False





    for i in build_frame:
        # 설치일 때 
        # isOk가 참이면 append
        if i[3] == 1 and isOk(i[:3]): 
            answer.append(i[:3])
            
        # 철거일 때,             
        elif i[3] == 0:
            x = i[0]
            y = i[1]
            # 철거했을 때 영향을 받는 구조들
            # near = [[x-1, y, 1], [x+1, y, 1], [x, y-1, 0], [x, y, 0], [x-1, y-1, 0], [x+1, y, 0]]
            near = [[x-1, y, 1], [x+1, y, 1], [x, y-1, 0], [x, y, 0], [x-1, y-1, 0], [x+1, y, 0]]
            
            # 철거해보고나서 주변 구조물이 괜찮은지 확인 해보고
            # 안 괜찮으면 다시 추가 (철거 실행 X)
            answer.remove(i[:3])
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
            for j in near:
                if not isOk(j): 
                    answer.append(i[:3])
                    break


    answer.sort()
    print(answer)
    return answer


# li = 	[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]

# solution(5, li)

# answer = [[1, 0, 0], [1, 1, 1]]
# def isOk(i):
#     if i[2] == 0:
#     # 기둥이 바닥 위에 있는 경우
#         if i[1] == 0:
#             return True        
#         for j in answer:
#             # 보의 한쪽 끝부분에 있는 경우 
#             # 보와 y좌표가 같을 때 
#             if j[2] == 1 and j[1] == i[1]:
#                 # 보와의 x좌표 기준도 충족할 때
#                 if j[0] == i[0]+1 or j[0] == i[0]:
#                     return True
#             # 다른 기둥 위에 있는 경우 : (x, y+1)
#             if j[2] == 0 and j[0] == i[0] and j[1] == i[1]+1:
#                 return True

#     # 보일 때   
#     elif i[2] == 1:
#         # 한쪽 끝부분이 기둥 위에 있는 경우 : 새로운 보의 기준에서 (x, y+1) 또는 (x-1, y+1)
#         if [i[0], i[1]-1, 0] in answer or [i[0]+1, i[1]-1, 0] in answer:
#             return True
#         # 양쪽 끝부분이 다른 보와 동시에 연결되어 있는 경우 : 새로운 보의 기준에서 좌표에서 각각 (x+1, y), (x-1, y)
#         elif [i[0]+1, i[1], 1] in answer and [i[0]-1, i[1], 1] in answer:
#             return True
    
#     # 조건이 충족되지 않을 때
#     return False``

# # print(isOk([2, 1, 0]))

# j = [1, 1, 1]
# i = [2, 1, 0]
# if j[2] == 1 and j[1] == i[1]:
#     # 보와의 x좌표 기준도 충족할 때
#     if j[0] == i[0]-1 or j[0] == i[0]:
#         print(True)
# # 다른 기둥 위에 있는 경우 : (x, y+1)
# if j[2] == 0 and j[0] == i[0] and j[1] == i[1]+1:
#     print(True)


