# dfs + 백트래킹

import sys
input = sys.stdin.readline


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(x, y, cnt):
    global answer
    if cnt == 26:
        answer = 26
        return
    else:
        answer = max(answer, cnt)
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < r and 0 <= ny < c:
            if visited[char_to_num(nx, ny)] == 0:
                visited[char_to_num(nx, ny)] = 1
                dfs(nx, ny, cnt + 1)
                visited[char_to_num(nx, ny)] = 0


def char_to_num(x, y):
    return ord(arr[x][y]) - ord('A')

r, c = map(int, input().split())
arr = [list(map(str, input().strip())) for _ in range(r)]
answer = 0
visited = [0] * 26
visited[char_to_num(0, 0)] = 1
dfs(0, 0, 1)

print(answer)