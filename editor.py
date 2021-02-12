from sys import stdin
 
stack1 = list(stdin.readline().strip())
stack2 = []
n = int(stdin.readline())

for command in stdin:
    if command[0] == 'L':
        if stack1: stack2.append(stack1.pop())
        else: continue
    elif command[0] == 'D':
        if stack2: stack1.append(stack2.pop())
        else: continue
    elif command[0] == 'B':
        if stack1: stack1.pop()
        else: continue
    elif command[0] == 'P':
        stack1.append(command[2])
print(''.join(stack1 + list(reversed(stack2))))