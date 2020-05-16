def dfs(y, x, matrix):
    matrix[y][x] = 0
    dy, dx = [0, 0, -1, 1], [-1, 1, 0, 0]
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < m and matrix[ny][nx]:
            dfs(ny, nx, matrix)
    return

import sys
sys.setrecursionlimit(10**8)
read = lambda : sys.stdin.readline().strip()

T = int(read())
for _ in range(1, T + 1):
    m, n, k = map(int, read().split()) # 가로 길이, 세로 길이, 위치 개수
    matrix = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        x, y = map(int, read().split())
        matrix[y][x] = 1
    Cnt = 0
    for i in range(m):
        for j in range(n):
            if matrix[j][i] == 1:
                Cnt += 1
                dfs(j, i, matrix)

    print(Cnt)