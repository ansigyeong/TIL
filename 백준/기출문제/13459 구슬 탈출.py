# BFS
from sys import stdin
from collections import deque
input = stdin.readline


N, M = map(int, input().split()) # 세로, 가로
board = [list(input().strip()) for _ in range(N)]
Q = deque()
visit = [[[[False]*M for _ in range(N)] for _ in range(M)] for _ in range(N)]
dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)

def init():
    _rx, _ry, _bx, _by = [0]*4
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                _rx, _ry = i, j
            elif board[i][j] == 'B':
                _bx, _by = i, j
    Q.append((_rx, _ry, _bx, _by, 0))
    visit[_rx][_ry][_bx][_by] = True

def move(_x, _y, _dx, _dy, _c):
    while board[_x+_dx][_y+_dy] != '#' and board[_x][_y] != 'O': # 0이 아니라 O임!!! 잘 보기!!!
        _x += _dx
        _y += _dy
        _c += 1
    return _x, _y, _c

def bfs():
    while Q:
        rx, ry, bx, by, d = Q.popleft()
        if d >= 10:
            break
        for i in range(4):
            nrx, nry, rc = move(rx, ry, dx[i], dy[i], 0)
            nbx, nby, bc = move(bx, by, dx[i], dy[i], 0)
            if board[nbx][nby] == 'O':
                continue
            if board[nrx][nry] == 'O':
                print(1)
                return
            if nrx == nbx and nry == nby:
                if rc > bc:
                    nrx, nry = nrx-dx[i], nry-dy[i]
                else:
                    nbx, nby = nbx-dx[i], nby-dy[i]
            if not visit[nrx][nry][nbx][nby]:
                visit[nrx][nry][nbx][nby] = True
                Q.append((nrx, nry, nbx, nby, d+1))
    print(0)

init()
bfs()

