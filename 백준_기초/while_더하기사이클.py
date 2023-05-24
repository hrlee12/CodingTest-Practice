# while_더하기사이클.py

"""
입력 : 정수
출력 : 입력된 수로 돌아오기까지의 사이클 수
기능 : 수의 첫째자리수 + 각 자릿수를 더한 수의 첫째자리수 -> 새로운 숫자 (반복)
"""




initial_num = int(input())
num = initial_num
count = 0

while True:
    count += 1
    first = num // 10
    second = num % 10
    tmp = first + second
    tmp_second = tmp % 10
    num = second * 10 + tmp_second
    if num == initial_num: break



print(count)
