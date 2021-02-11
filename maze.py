from sys import stdin

# 인접행렬 초기화
n, m = map(int, stdin.readline().split())
matrix = [stdin.readline().rstrip() for _ in range(n)]
visited = [[0]*m for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

# bfs
queue = [(0,0)]
visited[0][0] = 1

while queue:
    x, y = queue.pop(0)

    # 최종 경로 도달
    if x == n-1 and y == m-1:
        print(visited[x][y])
        break

    # 미로 이동
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if visited[nx][ny] == 0 and matrix[nx][ny] == '1':
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx,ny))