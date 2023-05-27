from collections import deque

queue = deque()

queue.append(5)
queue.append(3)
queue.append(2)
queue.popleft()

print(queue[1])



# print(queue[:1])
# 인덱스로 호출하는 건 되지만 인덱스 슬라이스는 안 됨. 
#queue.sort()    
# sort도 안 됨. 

# reverse는 됨 
queue.reverse()
print(queue)
print(queue.index(3))
print(type(queue))

# for문 돌아감. 
for i in queue:
    print(i)
    
    
print(list(queue))


# 반복가능한 자료형은 전부 다 입력값으로 넣어 초기화 가능. 
queue = deque([1, 2, 3])
print(queue)
queue = deque('1234')
print(queue)
queue = deque((1, 2, 3))
print(queue)
queue = deque({1, 2, 3})
print(queue)
queue = deque({'one':1, 'two':2, 'three':3})
print(queue)

print(list({'one':1, 'two':2, 'three':3}))



# list로도 queue구현 가능하지만 속도가 비교적 느림. 
# 큐에서의 삭제에 대한 인터페이스도 없으니 collections.deque가 훨씬 나음. 

li = [ 1, 2, 3]
print(li)

del li[0]

print(li)