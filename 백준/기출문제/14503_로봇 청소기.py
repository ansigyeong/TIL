import sys
from collections import deque

# 북 동 남 서
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

# 방향 전환
def change(dirs):
    if dirs == 0: # 북 => 서
        return 3
    elif dirs == 1: # 동 => 북
        return 0
    elif dirs == 2: # 남 => 동
        return 1
    elif dirs == 3: # 서 => 남
        return 2

# 후진
def back(dirs):
    if dirs == 0: # 북 => 남
        return 2
    elif dirs == 1: # 동 => 서
        return 3
    elif dirs == 2: # 남 => 북
        return 0
    elif dirs == 3: # 서 => 동
        return 1


def bfs(row, col, dirs):
    clean_cnt = 1
    arr[row][col] = 2
    q = deque([[row, col, dirs]])

    while q:
        row, col, dirs = q.popleft()
        temp_dirs = dirs

        for i in range(4):
            temp_dirs = change(temp_dirs)
            new_row, new_col = row + dy[temp_dirs], col + dx[temp_dirs]

            # a. 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
            if 0 <= new_row < N and 0 <= new_col < M and arr[new_row][new_col] == 0:
                clean_cnt += 1
                arr[new_row][new_col] = 2
                q.append([new_row, new_col, temp_dirs])
                break

            # c. 네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
            elif i == 3:
                new_row, new_col = row + dy[back(dirs)], col + dx[back(dirs)]
                q.append([new_row, new_col, dirs])

                # d. 네 방향 모두 청소가 이미 되어있거나 벽이면서, 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.
                if arr[new_row][new_col] == 1:
                    return clean_cnt


N, M = map(int, sys.stdin.readline().split()) # 세로, 가로
r, c, d = map(int, sys.stdin.readline().split()) # 로봇 위치, 방향
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

print(bfs(r, c, d))

