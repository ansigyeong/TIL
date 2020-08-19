import sys
from collections import deque


# 북, 동, 남, 서
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def change(dirs):
    if dirs == 0: # 북 => 서
        return 3
    elif dirs == 1: # 동 => 북
        return 0
    elif dirs == 2: # 남 => 동
        return 1
    elif dirs == 3: # 서 => 남
        return 2

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
        temp_dir = dirs
        for i in range(4):
            temp_dir = change(temp_dir)
            new_row, new_col = row + dy[temp_dir], col + dx[temp_dir]

            if 0 <= new_row < n and 0 <= new_col < m and arr[new_row][new_col] == 0:
                clean_cnt += 1
                arr[new_row][new_col] = 2
                q.append([new_row, new_col, temp_dir])
                break

            elif i == 3:
                new_row, new_col = row + dy[back(dirs)], col + dx[back(dirs)]
                q.append([new_row, new_col, dirs])

                if arr[new_row][new_col] == 1:
                    return clean_cnt


n, m = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

print(bfs(r, c, d))
