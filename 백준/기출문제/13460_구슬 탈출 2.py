def bfs(maps, r_start, b_start, head, cnt):
    global minValue
    if cnt > 10:
        return

    # 변수 초기화
    ry, rx = r_start
    by, bx = b_start
    dy, dx = head
    r_cnt, b_cnt = 0, 0
    r_out, b_out = False, False

    # 구현
    ny, nx = ry + dy, rx + dx
    while 0 <= ny < n and 0 <= nx < m:
        r_cnt += 1
        if maps[ny][nx] == 'O':
            r_out = True
            break
        elif maps[ny][nx] == '#':
            r_cnt -= 1
            r_start = ry, rx
            break
        elif maps[ny][nx] == '.':
            ry, rx = ny, nx
            ny, nx = ry + dy, rx + dx

    ny, nx = by + dy, bx + dx
    while 0 <= ny < n and 0 <= nx < m:
        b_cnt += 1
        if maps[ny][nx] == 'O':
            b_out = True
            break
        elif maps[ny][nx] == '#':
            b_cnt -= 1
            b_start = by, bx
            break
        elif maps[ny][nx] == '.':
            by, bx = ny, nx
            ny, nx = by + dy, bx + dx

    # 결과
    if r_start == b_start:
        if r_cnt > b_cnt:
            r_start = ry - dy, rx - dx
        else:
            b_start = by - dy, bx - dx

    if b_out:
        return
    elif r_out:
        minValue = min(cnt, minValue)
        return
    elif r_cnt == b_cnt == 0:
        return
    else:
        bfs(maps, r_start, b_start, (-1, 0), cnt + 1)
        bfs(maps, r_start, b_start, (1, 0), cnt + 1)
        bfs(maps, r_start, b_start, (0, -1), cnt + 1)
        bfs(maps, r_start, b_start, (0, 1), cnt + 1)


import sys
n, m = map(int, sys.stdin.readline().split())
maps = []
for y in range(n):
    arr = list(sys.stdin.readline().strip())
    maps.append(arr)
    for x in range(m):
        if arr[x] == 'R':
            r = (y, x)
            arr[x] = '.'
        elif arr[x] == 'B':
            b = (y, x)
            arr[x] = '.'

minValue = float('inf')
dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]

for head in dirs:
    bfs(maps, r, b, head, 1)

if minValue == float('inf'):
    print(-1)
else:
    print(minValue)