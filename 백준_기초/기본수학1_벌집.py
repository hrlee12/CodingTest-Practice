
room = int(input())


if room == 1:
    x = 1
else:
    num = 1
    x = 1
    while True:
        x += 1
        num += 6 * (x-1)
        if num >= room: break

print(x)
