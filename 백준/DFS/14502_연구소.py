# 완전 탐색
import sys
import copy


# 1. 벽 세우기 => 조합
def setWall(start, depth):
    global maxVal

    if depth == 3:
        # 복사
        copied = copy.deepcopy(Map)

        length = len(virusList)
        for i in range(length):
            [virusX, virusY] = virusList[i]
            spreadVirus(virusX, virusY, copied)

        maxVal = max(maxVal, getSafeArea(copied))
        return

    for i in range(start, N*M):
        x = i // M
        y = i % M

        if Map[x][y] == 0:
            Map[x][y] = 1
            setWall(i + 1, depth + 1)
            Map[x][y] = 0


# 2. 바이러스 퍼트리기 => DFS
def spreadVirus(x, y, copied):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            if copied[nx][ny] == 0:
                copied[nx][ny] = 2
                spreadVirus(nx, ny, copied)


# 3. 안전구역 넓이 구하기
def getSafeArea(copied):
    safe = 0
    for i in range(N):
        for j in range(M):
            if copied[i][j] == 0:
                safe += 1
    return safe


read = lambda : sys.stdin.readline().strip().split()
N, M = map(int, read()) # 세로, 가로
Map = [list(map(int, read())) for _ in range(N)]
virusList = []
for i in range(N):
    for j in range(M):
        if Map[i][j] == 2:
            virusList.append([i, j])
maxVal = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

setWall(0, 0)
print(maxVal)