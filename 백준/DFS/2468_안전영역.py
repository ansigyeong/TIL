import sys
sys.setrecursionlimit(10**8)
import copy


def dfs(x, y, copyArr):
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < n and copyArr[nx][ny]:
            copyArr[nx][ny] = 0 # 방문 체크
            dfs(nx, ny, copyArr)


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
maxList = []
result = 1
for i in range(n):
    maxList.append(max(arr[i]))
maxValue = max(maxList)
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for height in range(1, maxValue + 1):
    copyArr = copy.deepcopy(arr)
    for i in range(n):
        for j in range(n):
            if copyArr[i][j] <= height:
                copyArr[i][j] = 0
    count = 0
    for x in range(n):
        for y in range(n):
            if copyArr[x][y]:
                dfs(x, y, copyArr)
                count += 1
    if result < count:
        result = count

print(result)