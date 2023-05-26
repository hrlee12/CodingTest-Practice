import time

start_time = time.time()
array = [i for i in range(10000)]
array.reverse()

for i in range(len(array)-1):
    min_index = i
    for j in range(i+1, len(array)):
        if array[j] < array[min_index]:
            min_index = j
    array[min_index], array[i] = array[i], array[min_index]


# 내장함수와 속도 비교해보기
# 데이터가 10000개일 때, min함수와 index함수로 찾는게 4배 빠름
# for i in range(len(array)-1):
#     min_one = min(array[i:]) 
#     min_index = array.index(min_one)
#     array[min_index], array[i] = array[i], array[min_index]



# 데이터가 10000개일 때, sort함수로 정렬하는게 500배는 빠름
# 내장함수는 c언어로 만들어져있기 때문.
# array.sort()

print(array)



# 최솟값 찾기 : for문 vs min함수 
# 데이터가 10000개일 때, min함수가 2.5배 빠름
# 그니까 내장함수로 처리할 수 있는 건 내장함수로 처리하는 게 훠얼씬 좋음 !!!!!
# min_one = array[0]
# for i in array[1:]:
#     if i < min_one: min_one = i
 
# min_one = min(array)  

  


end_time = time.time()

print(f'{end_time - start_time} sec') 