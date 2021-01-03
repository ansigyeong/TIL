def dfs(v, visit):
    visit += [v]
    stack = []


n, m = map(int, input().split()) # 세로, 가로

matrix = [list(map(int, input())) for _ in range(n)]

# 위, 아래, 좌, 우
dn = [-1, 1, 0, 0]
dm = [0, 0, -1, 1]

startN, startM = 0, 0

dfs(startN, startM, [])
