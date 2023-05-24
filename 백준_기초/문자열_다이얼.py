# 문자열_다이얼


"""
입력값: 각 숫자를 나타내는 알파벳모음
기능 : 주어진 알파벳에 해당하는 숫자를 찾아 전화거는 데 걸리는 총 시간을 계산 
출력값 : 전화거는 데 걸리는 시간


해결해야 할 것
알파벳을 어떻게 숫자로 바꿀 것인가?

ABC - 2
DEF - 3
GHI - 4

아스키 코드 값이 65부터 90. 65빼면 0 ~ 25
ord(alpha) - 65의 값이
0~2   -> 2
3~5   -> 3
6~8   -> 4
9~11  -> 5
12~14 -> 6
15~18 -> 7
19~21 -> 8
22~25 -> 9

숫자는 알았고 그 숫자를 치는데 걸리는 시간이
1번 -> 2초. 2번 -> 2+1초  3번->2+1+1초. 1초씩 늘어남


내 답안
"""

data = input()
result = 0
for i in data:
    order = ord(i) - 65
    if   order <= 2:  result += 3
    elif order <= 5:  result += 4
    elif order <= 8:  result += 5
    elif order <= 11: result += 6
    elif order <= 14: result += 7
    elif order <= 18: result += 8
    elif order <= 21: result += 9
    else:             result += 10

print(result)



"""
다른 사람 답안

data = input()
alpha = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
result = 0
for i in data:
    for j in range(len(alpha)):
        if i in alpha[j]:
            result += j + 3

print(result)
"""

