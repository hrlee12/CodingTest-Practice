# deque는 deque()로 deque 객체를 생성해서 사용. 
# ex) queue = deque()   queue.popleft() 

# heapq는 그냥 배열에다가 heapq.heappush, heapq.heappop메서드를 이용해 삽입, 삭제하여 heap구현. 
# ex) array = []    heapq.heaqpush(array, 2)    heapq.heaqpop(array)


import heapq


heap = [5, 3, 2]


# 삽입할 때도 자기 나름의 기준으로 전체에 대해 정렬. 
# 근데 전체에 대해 힙이 엄격하게 적용된 것 같진 않다. 
heapq.heappush(heap, 2)
print(heap)

heapq.heappush(heap, 1)
print(heap)

heapq.heappush(heap, 4)
print(heap)


# 삭제할 때도 자기 나름의 기준으로 전체에 대해 정렬.  
# 근데 전체에 대해 힙이 엄격하게 적용된 것 같진 않다. 
# 그치만 일단 가장 작은 애가 삭제되는 건 맞음. 이것만 지키면 되지 뭐.
# 내부 동작은 라이브러리가 알아서 할테니 결론적으로 최솟값이 나오면 됨 !!!

print(heapq.heappop(heap))
print(heap)
print(heapq.heappop(heap))
print(heap)





array = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
print('heappush으로 삽입하지 않은 배열에 대해서 heappop해보기')
# 애초에 넣을 때부터 heappush로 정렬하면서 넣어줘야 heappop했을 때 제일 작은 수부터 나옴. 
print(heapq.heappop(array))
print(heapq.heappop(array))
print(heapq.heappop(array))



# 값을 넣을 때부터 heappush로 넣고 heappop해보기 
array = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]

heap = []
for i in array:
    heapq.heappush(heap, i)

print('넣을 때부터 heappush로 제대로 해주기')
for i in range(len(heap)):
    print(heapq.heappop(heap))


# heapq 라이브러리는 최소힙만 됨. (제일 작은 수가 먼저 나옴)
# 최대힙을 구현하기 위해서는 값을 삽입할 때 부호를 바꿔서 넣고 삭제할 때 다시 부호를 바꿔 사용. 
# ex) 2, 3, 4 -> -2, -3, -4   -4가 가장 작은 수이므로 가장 먼저 나옴. 
#  -4, -3, -2 순서로 나오는데 부호를 다시 바꾸면 4, 3, 2가 됨. -> 최대힙 구현가능. 

heap = []
for i in array:
    heapq.heappush(heap, -i)

print('최대힙 구현하기')
for i in range(len(heap)):
    print(-heapq.heappop(heap))