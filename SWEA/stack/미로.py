def Maze(y, x):
    global flag, N

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    maze[y][x] = 9

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if ny < 0 or ny == N:
            continue
        if nx < 0 or nx == N:
            continue
        if maze[ny][nx] == 1:
            continue
        if maze[ny][nx] == 9:
            continue
        if maze[ny][nx] == 3:
            flag = 1
            return
        Maze(ny, nx)

def findStart(data):
    global N
    for y in range(N):
        for x in range(N):
            if maze[y][x] == 2:
                return y, x

import sys
sys.stdin = open('미로.txt')

T = int(input())

for tc in range(1, T+1):
    flag = 0
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    sy, sx = findStart(maze)
    Maze(sy, sx)

    print('#{} {}'.format(tc, flag))