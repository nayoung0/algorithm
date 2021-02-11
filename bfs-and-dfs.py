from sys import stdin
n, m, v = map(int, stdin.readline.split())

# 인접행렬 관계 표시
matrix = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    line = list(map(int, stdin.readline.split()))
    matrix[line[0]][line[1]] = 1
    matrix[line[1]][line[0]] = 1

# 너비 우선 탐색
def bfs(start):
    visited = [start]
    queue = [start]
    while queue:
        n = queue.pop(0)
        for c in range(len(matrix[start])):
            if matrix[n][c] == 1 and (c not in visited):
                visited.append(c)
                queue.append(c)
    return visited

# 깊이 우선 탐색
def dfs(start, visited):
    visited += [start]
    for c in range(len(matrix[start])):
        if matrix[start][c] == 1 and (c not in visited):
            dfs(c, visited)
    return visited

print(*dfs(v,[]))
print(*bfs(v))
