# 기본수학1_손익분기점



A, B, C = (map(int, input().split()))

if B >= C:
    x = -1
else:
    x = A//(C-B)
    x += 1

print(x)
        
    

