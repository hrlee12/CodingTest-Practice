try:
    num = [1, 2, 3, 4, 5]
    a = 0
    while True:
        print(num[a])
        a += 1
except IndexError as e:
    print(e)
