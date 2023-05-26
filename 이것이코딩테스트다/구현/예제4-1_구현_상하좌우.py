import sys

size = int(sys.stdin.readline())
directions = sys.stdin.readline().split()

pos = {'x' : 1, 'y' : 1}
print(pos['x'])
print(pos['y'])
for d in directions:
    if (d == 'R') and pos['x'] < size:
        pos['x'] += 1
    elif (d == 'L') and pos['x'] > 1:
        pos['x'] -= 1
    elif (d == "U") and pos['y'] > 1:
        pos['y'] -= 1
    elif (d == "D") and pos['y'] < size:
        pos['y'] += 1
        
print(pos['y'], pos['x'])