# 정석 퀵정렬보단 조금 느리지만
# 파이썬의 장점을 살린 직관적인 퀵 정렬 


array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

# 정석과 다르게 탐색할 대상인 배열을 잘라서 입력함. 
def quick_sort(array):
    if len(array) <= 1:
        return array
    
    # 피봇과 나머지 분리
    pivot = array[0]
    tail = array[1:]
    
    # 테일에서 피봇보다 작은 것들의 배열을 리스트 내포로 만듦. 
    left_side = [x for x in tail if x <= pivot]
    # 테일에서 피봇보다 큰 것들의 배열을 리스트 내포로 만듦. 
    right_side = [x for x in tail if x > pivot]
    
    # 피봇의 크기를 기준으로 나눠진 왼쪽, 오른쪽 배열에 대해서도 각각 퀵 정렬 실행하면서
    # 동시에 합쳐서 리턴 
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)