from bisect import bisect_left, bisect_right

array = [1, 2, 3, 3, 3, 4]

print(bisect_left(array, 3))
print(bisect_right(array, 3))
