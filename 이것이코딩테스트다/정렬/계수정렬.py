# 계수정렬 (count sort)

# 정렬하려는 배열의 모든 값을 인덱스로 나타낸 count배열을 만들고 
# 인덱스에 해당하는 값의 갯수로 count배열의 값을 바꾼다. 
# 선택, 삽입, 퀵 정렬이 데이터의 값을 비교해서 위치를 변경했던 것과 다른 방식 

# 조건
# 1) 데이터가 정수여야 함. 범위가 무한한 실수는 인덱스로 일일이 표현 못 함.
# 2) 가장 큰 수와 가장 작은 수의 차이가 1,000,000을 넘지 않아야 함.
#    넘으면 속도가 많이 느려짐. 
# 데이터의 갯수는 상관 없음! 엄청 많아도 됨!


# 시간 복잡도
# 모든 데이터가 양수이고 가장 큰 수가 k라고 할 때 O(N+k)
# count에 표시할 때 N + 출력할 때 k
# 되게 빠르고 효율적인 알고리즘이지만 데이터가 0, 999,999 단 두개만 있을 때도 길이가 999,999개의 배열을 만들어야 됨. 다른 알고리즘에 비해 되게 비효율적이다. 
# 데이터의 크기가 한정되어 있고 겹치는 데이터가 많으면 유리함. 
# ex)시험 성적
# 데이터의 특성을 파악하기 어려우면 퀵 정렬을 사용하자. 
# 정렬 라이브러리(sort, sorted)는 퀵+병렬 정렬으로 O(NlogN)의 속도를 보장하니까 웬만하면 이걸로 쓰고 
# 데이터의 범위가 한장되어 있으며 더 빠르게 동작해야 할 때만 계수 정렬을 사용하자. 


# 모드 원소의 값이 0보다 크거나 같다고 가정 
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

# 각 인덱스의 해당하는 값의 수를 저장하는 count 배열 생성 
# ex) 최솟값이 0일 때, 최댓값이 9이면 0~9를 나타낼 수 있게 10개의 원소 필요. 
count = [0] * (max(array) + 1) 

for i in array:
    count[i] += 1
    

for i in range(len(count)):
    for _ in range(count[i]):
        print(i, end=' ')
