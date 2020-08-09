import sys
import collections


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


def rotate(s, d):
    if s == 'L':
        return (d + 3) % 4 # 왼쪽
    else:
        return (d + 1) % 4 # 오른쪽

def snake_move(direction):
    [x, y] = snake[0]

    nx = x + dx[direction]
    ny = y + dy[direction]

    # 머리가 몸통에 부딪히면 종료
    if [nx, ny] in snake:
        return True
    # 벽에 부딪히면 종료
    elif nx <= 0 or nx > N or ny <= 0 or ny > N:
        return True
    # 이동한 칸에 아무것도 없으면 꼬리를 자름
    elif arr[nx][ny] == 0:
        [ex, ey] = snake.pop()
        arr[ex][ey] = 0
    # 이동한 칸에 사과가 있으면 없애고 몸을 늘림
    snake.appendleft([nx, ny])
    arr[nx][ny] = 1
    return False


N = int(sys.stdin.readline()) # board 크기
K = int(sys.stdin.readline()) # 사과 수
arr = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(K):
    x, y = map(int, sys.stdin.readline().split())
    arr[x][y] = 2

L = int(sys.stdin.readline()) # the number of times the snake makes a turn
move = []
for _ in range(L):
    X, C = sys.stdin.readline().split() # X초, 방향(C) => L은 왼쪽, D는 오른쪽
    move.append([int(X), C])

# 뱀의 위치
arr[1][1] = 1
snake = collections.deque([[1, 1]])


# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

solve(move, L)