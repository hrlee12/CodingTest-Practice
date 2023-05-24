import sys

case_num = int(sys.stdin.readline())
stack = []


for i in range(case_num):
    command = sys.stdin.readline()
    command = command.split()
    if (command[0] == 'push'):
        stack.append(command[1])
    elif (command[0] == 'pop'):
        if (len(stack)>0): print(stack.pop())
        else: print(-1)
    elif (command[0] == 'size'):
        print(len(stack))
    elif (command[0] == 'empty'):
        if (len(stack)>0): print(0)
        else: print(1)
    elif (command[0] == 'top'):
        if (len(stack)>0): print(stack[-1])
        else: print(-1)
        


# import sys
# n = int(sys.stdin.readline())

# stack=[]
# for i in range(n):
#     command = sys.stdin.readline().split()

#     if command[0]=='push':
#         stack.append(command[1])
#     elif command[0]=='pop':
#         if len(stack)==0:
#             print(-1)
#         else:
#             print(stack.pop())
#     elif command[0] == 'size':
#         print(len(stack))
#     elif command[0] == 'empty':
#         if len(stack)==0:
#             print(1)
#         else:
#             print(0)
#     elif command[0] == 'top':
#         if len(stack)==0:
#             print(-1)
#         else:
#             print(stack[-1])