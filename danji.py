from sys import stdin
n = int(input())
matrix = [[0]*n for _ in range(n)]
visited = [[0]*n for _ in range(n)]

for i in range(n):
    line = stdin.readline().strip()
    for j, b in enumerate(line):
        matrix[i][j] = int(b)

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, c):
    visited[x][y] = 1
    global nums
    if matrix[x][y] == 1:
        nums += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if visited[nx][ny] == 0 and matrix[nx][ny] == 1:
                dfs(nx,ny, c)

cnt = 1
numlist = []
nums=0
for a in range(n):
    for b in range(n):
        if matrix[a][b] == 1 and visited[a][b] == 0:
            dfs(a,b,cnt)
            numlist.append(nums)
            nums = 0

print(len(numlist))
for n in sorted(numlist):
    print(n)
