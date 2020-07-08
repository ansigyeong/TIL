def bfs(maps, start_r, start_b, dirs, cnt):
    global minValue
    if cnt > 10:
        return

    ## 변수 초기화
    # 1. 이동
    dy, dx = dirs

    ry, rx = start_r
    by, bx = start_b

    # 2. 정지하기까지 이동한 횟수 => 같은 위치에 있을 때 선후관계를 가리는 용도
    r_cnt, b_cnt = 0, 0

    # 3. 구슬이 빠져나갔는지 여부
    r_out, b_out = False, False

    ## 구현
    # 1. 빨간 공
    ny, nx = ry + dy, rx + dx
    while 0 <= ny < n and 0 <= nx < m:
        r_cnt += 1
        if maps[ny][nx] == 'O':
            r_out = True
            break
        elif maps[ny][nx] == '#':
            r_cnt -= 1
            start_r = (ry, rx)
            break
        elif maps[ny][nx] == '.':
            ry, rx = ny, nx
            ny, nx = ry + dy, rx + dx

    # 2. 파란공
    ny, nx = by + dy, bx + dx
    while 0 <= ny < n and 0 <= nx < m:
        b_cnt += 1
        if maps[ny][nx] == 'O':
            b_out = True
            break
        elif maps[ny][nx] == '#':
            b_cnt -= 1
            start_b = (by, bx)
            break
        elif maps[ny][nx] == '.':
            by, bx = ny, nx
            ny, nx = by + dy, bx + dx

    ## 결과
    # 1. 두 공이 같은 위치에서 겹친 경우
    if start_r == start_b:
        if r_cnt > b_cnt:
            start_r = (ry - dy, rx - dx)
        else:
            start_b = (by - dy, bx - dx)

    # 2. 공이 통과한 경우
    if b_out:
        return
    elif r_out:
        minValue = min(minValue, cnt)
        return
    elif r_cnt == b_cnt == 0:
        return
    else:
        bfs(maps, start_r, start_b, (0, 1), cnt + 1)
        bfs(maps, start_r, start_b, (0, -1), cnt + 1)
        bfs(maps, start_r, start_b, (1, 0), cnt + 1)
        bfs(maps, start_r, start_b, (-1, 0), cnt + 1)


import sys
# import math
# input = sys.stdin.readline()

n, m = map(int, sys.stdin.readline().split()) # 세로, 가로
maps = []
for y in range(n):
    arr = list(sys.stdin.readline().strip())
    maps.append(arr)
    for x in range(m):
        if arr[x] == 'R':
            r = (y, x)
            arr[x] = '.' # 맵을 재활용하기 위해 처음 위치값만 저장한 뒤 값을 .로 바꿈
        if arr[x] == 'B':
            b = (y, x)
            arr[x] = '.' # 맵을 재활용하기 위해 처음 위치값만 저장한 뒤 값을 .로 바꿈

minValue = float('inf')

dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]

for head in dirs:
    bfs(maps, r, b, head, 1)

if minValue == float('inf'):
    print(-1)
else:
    print(minValue)
