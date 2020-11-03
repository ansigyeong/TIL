import sys


def move(S):
    dir = [(0, 1), (0, -1), (1, 0), (-1, 0)] # y, x => 오른쪽, 왼쪽, 아래, 위
    if S == 'up' or S == 'left':
        st_idx, end_idx, step = 0, N, 1
        if S == 'up':
            dy, dx = dir[3]
        else:
            dy, dx = dir[1]
    else:
        st_idx, end_idx, step = N-1, -1, -1
        if S == 'down':
            dy, dx = dir[2]
        else:
            dy, dx = dir[0]

    canMerged = [[True] * N for _ in range(N)]

    for y in range(st_idx, end_idx, step):
        for x in range(st_idx, end_idx, step):
            ny = y + dy
            nx = x + dx
            if 0 <= ny < N and 0 <= nx < N:
                if arr[y][x] == 0:
                    continue
                elif arr[ny][nx] == 0:
                    
                    value = arr[y][x]
                    arr[ny][nx] = value
                    arr[y][x] = 0
                elif arr[y][x] == arr[ny][nx] and canMerged[ny][nx]:
                    canMerged[ny][nx] = False
                    arr[ny][nx] *= 2
                    arr[y][x] = 0










T = int(sys.stdin.readline())
N, S = sys.stdin.readline().split()
N = int(N)
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
