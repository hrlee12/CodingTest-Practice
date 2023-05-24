# for_별찍기.py


times = int(input())


for i in range(times):
    form = '%' + str(times) + 's'
    
    print(form % ('*'*(i+1)))




