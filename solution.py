import sys
from collections import deque
from copy import deepcopy

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def move(arr, dir):
    # canMerged[i][j]는 (i, j)번 째 블록이 합쳐질 수 있는지를 bool 타입으로 담음
    canMerged = [[True] * N for _ in range(N)]

    # 움직이는 방향에 따라, 반복문의 진행 방향이 다름
    # 위 또는 왼쪽으로 이동하는 경우
    if dir in [0, 3]:
        start_idx, end_idx, step = 0, N, 1
    else:
        start_idx, end_idx, step = N-1, -1, -1

    # 현재 판의 모든 좌표를 탐색하며, 움직임이 필요한 값들을 움직임
    for i in range(start_idx, end_idx, step):
        for j in range(start_idx, end_idx, step):
            if arr[i][j] == 0:
                continue # 아래 코드를 실행하지 않고 건너뜀
            x, y = i, j
            value = arr[x][y]
            arr[x][y] = 0
            nx, ny = x + dx[dir], y + dy[dir]
            while True:
                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    break
                if arr[nx][ny] == 0:
                    x, y = nx, ny
                    nx, ny = x + dx[dir], y + dy[dir]
                elif arr[nx][ny] == value and canMerged[nx][ny]:
                    x, y = nx, ny
                    canMerged[x][y] = False
                    break
                else:
                    break
            arr[x][y] = arr[x][y] + value
    return arr


def bfs(arr):
    """
    알고리즘 간략 설명
    1. bfs queue에 각 스텝에 따른 판 전체(arr)를 넣음
    2. queue에서 판을 하나씩 빼와서 네 방향으로 움직인 후의 판을 queue에 넣음
    3. 스텝이 다섯번째가 되었을 때, bfs를 강제로 종료함
    :param arr:
    :return:
    """
    q = deque(arr)
    max_value = -1
    step = 0

    while q:
        size = len(q)
        for _ in range(size):
            arr = q.popleft()

            for dir in range(4):
                # 새로운 판을 만들어야 하므로, 반드시 deepcopy 해야 함
                next_arr = move(deepcopy(arr), dir)
                q.append(next_arr)

                # 새로 만든 판에서 가장 큰 값을 조사함
                for i in range(N):
                    for j in range(N):
                        if next_arr[i][j] > max_value:
                            max_value = next_arr[i][j]

        step += 1

        # 다섯번 째 스텝일 때, 가장 큰 값을 반환함
        if step == 5:
            return max_value


N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

print(bfs(arr))