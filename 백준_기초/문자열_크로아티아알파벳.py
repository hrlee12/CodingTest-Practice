# 문자열_크로아티아알파벳





text = input()
alph = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in alph:
    text = text.replace(i, "*")     # <- 몇개 있든 해당 문자를 다 찾아서 바꿔버림.
print(len(text))                    #  dz=가 먼저 나와 z= 중복세기 방지

    
