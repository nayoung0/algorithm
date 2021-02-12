from sys import stdin

def push(x):
    stack.append(x)

def pop():
    if not stack:
        return -1
    else:
        return stack.pop()

def size():
    return len(stack)

def empty():
    return 0 if stack else 1

def top():
    return stack[-1] if stack else -1

command_size = int(stdin.readline().strip())
stack = []

for _ in range(command_size):
    command = stdin.readline().strip().split()
    if command[0] == "push":
        push(command[1])
    elif command[0] == "pop":
        print(pop())
    elif command[0] == "size":
        print(size())
    elif command[0] == "empty":
        print(empty())
    elif command[0] == "top":
        print(top())