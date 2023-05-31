def binary_search(array, target, start, end):
    if start > end:
        return 'no'
    middle = (start + end) // 2
    
    if array[middle] == target:
        return 'yes'
    elif array[middle] > target:
        return binary_search(array, target, start, middle-1)
    else:
        return binary_search(array, target, middle+1, end)
        
        
        
    

n = int(input())
nums = list(map(int, input().split()))

m = int(input())
targets = list(map(int, input().split()))

nums.sort()
for target in targets:
    answer = binary_search(nums, target, 0, n-1)
    print(answer, end=' ')