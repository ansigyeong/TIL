import sys
from collections import deque
from copy import deepcopy


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def move(arr, dir):
    canMerged = [[True] * N for _ in range(N)]

    if dir in [0, 3]:
        startIdx, endIdx, step = 0, N, 1
    else:
        startIdx, endIdx, step = N - 1, -1, -1

    for i in range(startIdx, endIdx, step):
        for j in range(startIdx, endIdx, step):
            if arr[i][j] == 0:
                continue
            x, y = i, j
            value = arr[x][y]
            


def bfs(arr):
    """
    알고리즘 간략 설명
    1. bfs queue에 각 스텝에 따른 판 전체(arr)를 넣음
    2. queue에서 판을 하나씩 빼와서 네 방향으로 움직인 후의 판을 queue에 넣음
    3. 스텝이 다섯번째가 되었을 때, bfs를 강제로 종료함
    :param arr:
    :return:
    """
    q = deque([arr])
    step = 0
    maxValue = -1

    while q:
        size = len(q)
        for _ in range(size):
            arr = q.popleft()
            for dir in range(4):
                nextArr = move(deepcopy(arr), dir)
                q.append(nextArr)

                tempMax = max(map(max, nextArr))
                if tempMax > maxValue:
                    maxValue = tempMax

         step += 1

        if step == 5:
            return maxValue


N = int(sys.stdin.readline().strip().split())
arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

print(bfs(arr))