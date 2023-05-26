
# 퀵 정렬
# 기준 데이터(pivot, 여기서는 첫번째 데이터)을 기준으로 작은 것은 왼쪽, 큰 것은 오른쪽으로 정렬하고 
# 왼쪽, 오른쪽 각각 정렬 실행. (재귀함수)
# 데이터가 하나가 되면 return

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


# 전체 배열, 시작 인덱스, 끝 인덱스 입력
def quick_sort(array, start, end) :
    print(array[start:end+1])
    if start >= end : 
        return
    pivot = start
    left = start+1
    right = end
    
    # 교차하면 피봇이랑 작은 거(right)랑 바꿈. 
    # 교차하기 전까지 반복
    while left <= right:
        # left가 end보다 작거나 같고 그 데이터의 값이 피봇보다 작을 때 계속 탐색( left += 1 )
        # left가 end보다 작을 때로 하면 같을 때 빠져나올텐데 
        # 그럼 [4, 3]의 경우에는 작은 것(3)과 인덱스가 같아 계속 둘을 바꾸게 되는 무한루프 참사가 일어남. 
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        # 교차하면 피봇과 right의 값을 바꿔 while문을 빠져나올 준비. 
        if left > right:
            array[pivot], array[right] = array[right], array[pivot]
        # 교차하지 않으면 left와 right의 값을 바꿈.     
        else:
            array[left], array[right] = array[right], array[left]
    
    # 피봇을 기준으로 왼쪽, 오른쪽에 대해서 재귀함수 실행.   
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)


quick_sort(array, 0, len(array)-1)
print(array)