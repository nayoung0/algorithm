from sys import stdin
read = stdin.readline
dict1 = {}
for i in range(int(read())):
    dict1[i+1] = set()
for j in range(int(read())):
    a, b = map(int,read().split())
    dict1[a].add(b)
    dict1[b].add(a)

def dfs(start, dict1):
    for i in dict1[start]:
        if i not in visited:
            visited.append(i)
            dfs(i, dict1)
visited = []
dfs(1, dict1)
print(len(visited)-1)