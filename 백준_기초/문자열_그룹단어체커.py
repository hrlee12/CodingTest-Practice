# 문자열_그룹체커

num = int(input())
words = []

for i in range(num):
    words.append(input())


result = 0

for i in words:
    exist = []
    not_group = False
    for j in i:
        if j in exist:
            if j == exist.pop():
                exist.append(j)
            else: not_group = True
        else:
            exist.append(j)
    if not_group: continue
    result += 1


print(result)
