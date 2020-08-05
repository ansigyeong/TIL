# 지도 좌표 (r, c); 북쪽으로부터 r 서쪽으로부터 c

# 지도에서 이동한 칸에 쓰여있는 수가 0이면, 주사위 바닥면에 쓰여 있는 수가 칸에 복사됨
# 지도에서 이동한 칸에 쓰여있는 수가 0이 아니면, 칸에 쓰여 있는 수가 주사위 바닥면으로 복사되고 칸은 0이 됨

# 주사위가 이동할 때 마다 상단에 쓰여 있는 값 구하기 (지도 바깥으로 이동하는 명령은 무시하고 출력도 하면 안 됨)

# 주사위의 움직임이 칸의 범위 내에 있는지 체크
def check(k):
    global print_check
    nx = x + dx[k]
    ny = y + dy[k]
    if 0 <= nx < N and 0 <= ny < M:
        print_check = 1
        return True
    else:
        return False


# 이동칸 숫자가 0일 때와 0이 아닐 때의 값 변화
def copy(k):
    if game_map[x + dx[k]][y + dy[k]] == 0:
        game_map[x + dx[k]][y + dy[k]] = dice[0]
    else:
        dice[0] = game_map[x + dx[k]][y + dy[k]]
        game_map[x + dx[k]][y + dy[k]] = 0


import sys


N, M, x, y, K = map(int, sys.stdin.readline().split()) # 지도 크기(세로, 가로), 주사위 좌표(세로,  가로), 명령 수
game_map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
heads = list(map(int, input().split())) # 이동 명령; 동 서 북 남 => 1 2 3 4

# 주사위 전개도; 1이 윗 면, 3이 동쪽

#   2
# 4 1 3
#   5
#   6

# 주사위 전개도 기준으로
# dice[0] => 1
# dice[1] => 5
# dice[2] => 6
# dice[3] => 2
# dice[4] => 4
# dice[5] => 3

dice = [0] * 6

# 시작 위치 설정
# dice[0] = game_map[x][y]

# -, 동, 서, 북, 남
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

print_check = 0

for i in range(K):
    # 각 움직임 체크
    if check(heads[i]):
        if heads[i] == 1: # 동쪽
            dice[0], dice[2], dice[4], dice[5] = dice[5], dice[4], dice[0], dice[2]
            copy(heads[i])

        elif heads[i] == 2: # 서쪽
            dice[0], dice[2], dice[4], dice[5] = dice[4], dice[5], dice[2], dice[0]
            copy(heads[i])

        elif heads[i] == 3: # 북쪽
            dice[0], dice[1], dice[2], dice[3] = dice[3], dice[0], dice[1], dice[2]
            copy(heads[i])

        elif heads[i] == 4: # 남쪽
            dice[0], dice[1], dice[2], dice[3] = dice[1], dice[2], dice[3], dice[0]
            copy(heads[i])

        if print_check:
            print(dice[2])
            x += dx[heads[i]]
            y += dy[heads[i]]
            print_check = 0