# 지도 좌표 (r, c); 북쪽으로부터 r 서쪽으로부터 c

# 주사위 전개도; 1이 윗 면, 3이 동쪽
#  2
# 413
#  5
#  6


# 지도에서 이동한 칸에 쓰여있는 수가 0이면, 주사위 바닥면에 쓰여 있는 수가 칸에 복사됨
# 지도에서 이동한 칸에 쓰여있는 수가 0이 아니면, 칸에 쓰여 있는 수가 주사위 바닥면으로 복사되고 칸은 0이 됨

# 주사위가 이동할 때 마다 상단에 쓰여 있는 값 구하기 (지도 바깥으로 이동하는 명령은 무시하고 출력도 하면 안 됨)

import sys

N, M, x, y, K = map(int, sys.stdin.readline().split()) # 지도 크기(세로, 가로), 주사위 좌표(세로,  가로), 명령 수
game_map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
heads = list(map(int, input().split())) # 이동 명령; 동 서 북 남 => 1 2 3 4

dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)] # 지도 이동 방향; 동 서 북 남
upperSideNumber = 0 # 가장 처음에 주사위는 모든 면이 0임

for head in heads:
    if head == 1:
        dy = dir[0][0]
        dx = dir[0][1]
    elif head == 2:
        dy = dir[1][0]
        dx = dir[1][1]
    elif head == 3:
        dy = dir[2][0]
        dx = dir[2][1]
    elif head == 4:
        dy = dir[3][0]
        dx = dir[3][1]
    print(upperSideNumber)