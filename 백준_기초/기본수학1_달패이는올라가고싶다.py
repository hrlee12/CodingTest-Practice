# 기본수학1_달팽이는올라가고싶다


A, B, V = map(int, input().split())



x = (V-B) / (A-B)


if x % 1 != 0:
    x = x // 1 + 1

print(int(x))



