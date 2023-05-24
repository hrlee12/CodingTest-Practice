# 문자열_그룹단어체커_2


num = int(input())

for i in range(num):
    word = input()
    num_alph = len(set(word))
    change = 0
    for i in range(len(word) - 1):
        if word[i] != word[i+1]: change += 1
    if change != num_alph - 1: num -= 1

print(num)

        
