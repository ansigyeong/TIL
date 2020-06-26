import sys
input = sys.stdin.readline


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def dfs(Rx, Ry, cnt):
    global Bx, By
    if cnt > 10:
        return -1
    else:
        # 상, 하, 좌, 우에 대해서 R, B 동시에 이동함
        for k in range(4):
            nRx = Rx + dx[k]
            nRy = Ry + dy[k]
            nBx = Bx + dx[k]
            nBy = By + dy[k]


        # 1. . 만났을때 => 계속 이동함
        # 2. #이나 R, B 만났을 때 => 멈춤
        # 3. 0 만났을 때 => R이면 최소인지 판단하고 return cnt, B이면 continue, 동시에 도착하면 이동거리 짧은 게 0 만난 것
        return cnt

# 빨간 구슬은 빼고 파란 구슬은 빼면 안됨
# break point => 구슬이 더 이상 움직이지 않을때
N, M = map(int, input().split()) # 세로, 가로 (크기 => N * M)

board = [list(input().strip()) for _ in range(N)]
# . => 이동 o, # => 이동 x, O => 구멍, R => 빨간 구슬, B => 파란 구슬

for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            Rx = i
            Ry = j
        elif board[i][j] == 'B':
            Bx = i
            By = j

maxCnt = 0
cnt = 0

dfs(Rx, Ry, cnt)

print(cnt)