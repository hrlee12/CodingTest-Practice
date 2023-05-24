# 기본수학1_설탕배달





"""
입력 : 배달할 설탕 무게
기능 : 봉지는 5kg, 3kg 두가지. 봉지수를 최소로 배달하자. 

출력 : 배달하는 봉지의 최소 개수.
        (정확하게 N킬로그램 불가능하면 -1 출력)


설탕 무게를 
5로 나눈 나머지가
1 
4 
+5하면 3의 배수
-> 5를 하나 덜 나눔.
    그냥 1, 4는 못 함

2 (+ 5 + 5)
+10하면 3의 배수
-> 5를 두개 덜 나눔.
    5가 두개인 12가 아니라 2, 7이다? 못 함. 



5로 나눈 나머지가
3
0
-> 5로 나누고 남은 나머지를 3으로 나눔. 

"""

num = int(input())

a = num // 5
remainder = num % 5

if remainder == 0 or remainder == 3:
    b = remainder // 3
    result = a + b
elif remainder == 1 or remainder == 4:
    a -= 1
    if a < 0:
        result = -1
    else:
        b = (remainder + 5) // 3
        result = a + b
else:
    a -= 2
    if a < 0:
        result = -1
    else:
        b = (remainder + 5*2) // 3
        result = a + b

print(result)


