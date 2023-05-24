# 함수_한수.py


"""
함수의 기능
입력값 : 양의 정수 N
기능 : 입력값의 각 자리가 등차수열을 이루는지(한수인지) 확인한다.
출력값 : 한수면 참/ 아니면 거짓을 출력한다.





"""

def hansu(num):
    if num < 100: return True
    
    sep_num = list(map(int, str(num)))
    
    if sep_num[1] - sep_num[0] == sep_num[2] - sep_num[1]:
        return True
    else:
        return False

        



num = int(input())
result = 0

for i in range(1, num+1):
    if hansu(i): result += 1

print(result)    







"""
수정전 : N이 1000보다 작다는 조건이 없을 때
def hansu(num):
    if num < 100: return True
    
    sep_num = list(map(int, str(num)))
    a, b = 0, 1
    gap = sep_num[b] - sep_num[a]
    try:
        while True:
            a += 1
            b += 1
            gap_2 = sep_num[b] - sep_num[a]
            if gap_2 != gap: return False
    except IndexError:
        pass
    return True
"""
