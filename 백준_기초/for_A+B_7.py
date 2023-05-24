# for_A+B_7


num = int(input())
numbers = []

for i in range(num):
   ab = map(int, input().split())
   numbers.append(ab)

count = 0
for a, b in numbers:
    count += 1
    print("Case #%d: %d" % (count, a+b))
