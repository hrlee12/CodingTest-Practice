# 중간값을 찾는 문제

n = int(input())
nums = list(map(int, input().split()))
nums.sort()
middle = n / 2 
if middle % 1 != 0:
    middle = middle // 1 + 1
middle = int(middle-1)

print(nums[middle])