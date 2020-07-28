N, M, x, y, K = map(int, input().split()) # 세로, 가로, 명령
game_map = list(list(map(int, input().split())) for _ in range(N))
head = list(map(int, input().split())) # 동 서 북 남 => 1 2 3 4

#  2
# 413
#  5
#  6

n, m = x, y
for _ in range(8):
    newN, newM =
    while 0 <= newN < 4 and 0 <= newM < 2:
