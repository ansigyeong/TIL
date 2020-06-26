import sys
read = lambda : sys.stdin.readline()
sys.setrecursionlimit(10**8)


def dfs(y, x, arr):
    global size
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0 <= ny < m and 0 <= nx < n and not arr[ny][nx]:
            size += 1
            arr[ny][nx] = 1 # 방문 체크
            dfs(ny, nx, arr)


m, n, k = map(int, read().strip().split()) # m: 세로(y), n: 가로(x) => m*n크기의 모눈종이, k개의 직사각형
arr = [[0 for _ in range(n)] for _ in range(m)]
for _ in range(k):
    x1, y1, x2, y2 = map(int, read().strip().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            arr[y][x] = 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
# pprint(arr)
cnt = 0
List = []

for y in range(m):
    for x in range(n):
        if not arr[y][x]:
            size = 1
            arr[y][x] = 1
            dfs(y, x, arr)
            cnt += 1
            List.append(size)

List = sorted(List)

print(cnt)
for _ in range(len(List)):
    print('{}'.format(List.pop(0)), end=" ")