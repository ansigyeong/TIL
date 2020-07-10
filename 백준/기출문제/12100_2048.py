def game(head, cnt):
    global maxValue
    if cnt == 0:
        maxNum = max(map(max, copyArr))
        if maxValue < maxNum:
            maxValue = maxNum
        return
    else:
        dy, dx = head
        for y in range(N):
            for x in range(N):
                ny = y + dy
                nx = x + dx
                if 0 <= ny < N and 0 <= nx < N:
                    if copyArr[ny][nx] == 0:
                        copyArr[ny][nx] = copyArr[y][x]
                        copyArr[y][x] = 0
                    elif copyArr[ny][nx] == copyArr[y][x] and check[ny][nx] == 0:
                        check[ny][nx] = 1
                        copyArr[ny][nx] *= 2
                        copyArr[ny][nx] = 0
        game((0, -1), cnt - 1)
        game((0, 1), cnt - 1)
        game((-1, 0), cnt - 1)
        game((1, 0), cnt - 1)

import sys
import copy


N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

cnt = 5
maxValue = 0
dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
for head in dirs:
    copyArr = copy.deepcopy(arr)
    check = [[0 for _ in range(N)] for _ in range(N)]
    game(head, cnt)

print(maxValue)