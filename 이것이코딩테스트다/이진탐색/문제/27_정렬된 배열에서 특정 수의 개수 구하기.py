# 값의 범위가 -10^9 <= x 10^9로 2억
# 데이터의 수는 100만으로 적지만 값의 범위가 크니 O(logN)의 시간 복잡도로 풀어야 함. 

# count()함수의 시간 복잡도는 O(N)
# 이진탐색으로 풀어야함. 

# 내가 생각한 풀이 
# 크기 순으로 배열되어 있으므로 타겟은 이웃해 있을 것. 
# 타겟의 위치를 이진탐색으로 찾고 좌우로 타겟이 있으면 count를 늘려가며 갯수를 체크한다. 
# 주어진 배열의 값이 전부 target이면 최악의 경우 O(logN + 1/2*N)의 시간 복잡도 -> 불완전한 풀이


# 타겟의 맨 왼쪽, 오른쪽 인덱스를 구하는 이진탐색 함수를 각각 만들어 해결한다. 
# bisect라이브러리를 이용하면 쉽게 해결가능. 


# 이진탐색
def binary_search(array, target, start, end):
    if start > end:
        return None
    
    middle = (start + end) // 2
    
    if array[middle] == target:
        return middle
    elif array[middle] > target:
        return binary_search(array, target, start, middle-1)
    else:
        return binary_search(array, target, middle+1, end)



n, x = map(int, input().split())
array = list(map(int, input().split()))

# 이진탐색 실행
answer = binary_search(array, x, 0, n-1)

# 타겟이 있으면 횟수 세기 
if answer:
    # 갯수
    count = 1
    # 왼쪽으로 진행하며 확인할 인덱스
    left = answer
    # 오른쪽으로 진행하며 확인할 인덱스
    right = answer
    
    while True:
        # while문을 반복할지 체크하는 변수
        # 양쪽 중 하나라도 있으면 True로 바꿈. 
        continue_of_iteration = False
    
        # 인덱스 바꿔줌.
        left -= 1
        # 왼쪽이 타겟이면
        if array[left] == array[answer]:
            # 반복 진행
            continue_of_iteration = True
            # 갯수 늘려줌. 
            count += 1

        # 오른쪽도 똑같이 실행
        right += 1
        if array[right] == array[answer]:
            continue_of_iteration = True
            count += 1
        
        # 양쪽 다 없으면 while문에서 벗어남. 
        if not continue_of_iteration:
            break
     
    print(count)
    
# 타겟이 없으면 -1 출력
else:
    print(-1)   
    
    
    
