def dfs(x, y, cnt, Map):
    Map[x][y] = 0
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < n and Map[nx][ny]:
            cnt = dfs(nx, ny, cnt+1, Map)
    return cnt

import sys
read = lambda : sys.stdin.readline().strip()
n = int(read())
Map = [list(map(int, read())) for _ in range(n)]
ans = []

for i in range(n):
    for j in range(n):
        if Map[i][j] == 1:
            ans.append(dfs(i, j, 1, Map))

print(len(ans))
for i in sorted(ans):
    print(i)