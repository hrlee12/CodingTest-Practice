def binary_search(array, target, start, end):
    middle = (start + end) // 2
    
    sum = 0
    for i in array:
        rest = i - middle
        if rest > 0:
            sum += rest
            
    if start == end:
        if sum < target: 
            return start-1
        elif sum > target:
            return start
            
    

    
    if sum == target:
        return middle
    elif sum > target:
        return binary_search(array, target, middle+1, end)
    else:
        return binary_search(array, target, start, middle-1)
        

n, m = (map(int, input().split()))
array = list(map(int, input().split()))
answer = binary_search(array, m, 0, max(array))

print(answer)