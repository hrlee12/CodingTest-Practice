def solution(my_string, overwrite_string, s):
    first = my_string[0:s]
    last = my_string[s+len(overwrite_string):]
    
    answer = first + overwrite_string + last
    return answer

print(solution("He11oWor1dnew", 'lloWorl', 2))


for i in range(10):
    print(i)
    
print(pow(2, 2))
print(pow(2, 4))


li = [1, 2, 3, 4]
print(li[-1])
print(li[-2])
a = 4
a /= 2
print(a)
a *= 4
print(a)
a -= 5
print(a)

dic = {'a':1, 'b':2}
print(list(dic.values()))
print(list(dic.keys()))

a = 5
a //= 2
print(2)


