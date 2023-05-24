# 기본수학_부녀회장이될테야

"""
2층
1 1+1+2 1+1+2+1+2+3

1층
1  1+2  1+2+3 ...

0층
1명 2명 3명 4명 5명

1, 2
1 + 2
2, 2




1, 2 -> 0, 2    0, 1
1, 1 -> 0, 1


"""




num = int(input())
data = []

for i in range(num):
    floor = int(input())
    roomnum = int(input())
    data.append([floor, roomnum])
    

print(data)    
               


for floor, roomnum in data:
    numlist = list(range(1, roomnum+1))
    for i in range(floor):
        tmp = [1]
        for j in range(1, roomnum):
            tmp.append(tmp[j-1]+numlist[j])
        numlist = tmp.copy()
    print(numlist[roomnum-1])            



"""
시간초과
def livingnum(floor, roomnum):
    if floor == 0:
        return roomnum
    result = 0
    while roomnum:
        result += livingnum(floor-1, roomnum)
        roomnum -= 1
    return result


num = int(input())
data = []

for i in range(num):
    tmp = []
    tmp.append(int(input()))
    tmp.append(int(input()))
    data.append(tmp)
               
for floor, roomnum in data:
    result = livingnum(floor, roomnum)
    print(result)        
"""
