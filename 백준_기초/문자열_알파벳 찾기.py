# 문자열_알파벳 찾기


data = input()

for i in range(97, 123):
    result = data.find(chr(i))
    
    print(result, end=' ')
