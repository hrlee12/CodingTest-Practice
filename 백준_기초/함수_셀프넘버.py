# 함수_셀프넘버


def Kaprekar(number):
    add = sum(map(int, str(number)))
    add_all = add + number
    return add_all

yes_creator = []

for i in range(1, 10001):
    yes_creator.append(Kaprekar(i))
    


for i in range(1, 10001):
   if i not in yes_creator: print(i)
