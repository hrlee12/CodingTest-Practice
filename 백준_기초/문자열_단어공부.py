# 문자열_단어공부


word = input().upper()      # 대소문자 구분 안 한다 했으므로 대문자로 전부 바꿈. 출력=대문자.
word_list = list(set(word))
count_list = []


for i in word_list:
    cnt = word.count(i)
    count_list.append(cnt)


if count_list.count(max(count_list)) > 1:
    print('?')
else:
    max_index = count_list.index(max(count_list))
    print(word_list[max_index])






"""
내 답안

word = input()
num_count = []
for i in range(26):
    num_count.append(word.count(chr(i+65)) + word.count(chr(i+97)))

num = max(num_count)
if num_count.count(num) == 1:
    askii = num_count.index(num)
    askii += 65
    print(chr(askii))
else:
    print('?')


        
    
"""
