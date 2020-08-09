# 시뮬레이션

# 사과의 위치와 뱀의 이동경로가 주어질 때, 게임이 끝나는 초(second) 구하기

# 조건
# 1. 뱀의 머리는 무조건 이동함
# 2. 뱀의 머리가 있는 곳
#       - 사과가 있으면 => 꼬리 위치 그대로
#       - 사과가 없으면 => 꼬리 자르기
#       - 벽이나 뱀의 몸이 있으면 => game over

def snake_move(direction):
    [x, y] = snakes[0]

    nx = x + dx[direction]
    ny = y + dy[direction]

    # 머리가 몸통에 부딪히면 종료
    if [nx, ny] in snakes:
        return True

    # 벽에 부딪히면 종료
    elif nx <= 0 or nx > N or ny <= 0 or ny > N:
        return True

    # 이동한 칸에 아무것도 없으면 꼬리를 자름
    elif arr[nx][ny] == 0:
        [ex, ey] = snakes.pop()
        arr[ex][ey] = 0

    # 이동한 칸에 사과가 있으면 없애고 몸을 늘림(뱀의 머리는 무조건 이동하므로 if문 안써도 됨)
    snakes.appendleft([nx, ny])
    arr[nx][ny] = 1

    return False


def rotate(s, d):
    if s == 'L':
        return (d + 3) % 4 # 왼쪽
    else:
        return (d + 1) % 4 # 오른쪽

def solve(move, L):
    idx = 0
    direction = 1 # 초기 방향은 오른쪽임
    time = 0

    while True:
        if idx < L:
            if move[idx][0] == time:
                direction = rotate(move[idx][1], direction)
                idx += 1

        if snake_move(direction) == True:
            print(time + 1)
            return

        time += 1


import sys
import collections

N = int(sys.stdin.readline()) # 크기
K = int(sys.stdin.readline()) # 사과 수
arr = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(K):
    i, j = map(int, sys.stdin.readline().split())
    arr[i][j] = 2

L = int(sys.stdin.readline()) # the number of times the snake makes a turn

move = []
for i in range(L):
    X, C = sys.stdin.readline().split() # X초 끝에 회전, C가 L => left, C가 D => right
    move.append([int(X), C])

# 북 동 남 서 (시계 방향)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 처음 뱀 위치
arr[1][1] = 1
snakes = collections.deque([[1, 1]])

solve(move, L)
