import sys


def bfs(maps, start_r, start_b, dirs, cnt):
    global mins
    if cnt > 10:
        return
    # check point
    # 1. 구슬이 이동할 수 없을 때 => break
    # 2. 파란 구슬이 빠졌을 때 => break
    # 3. 구슬이 동시에 구멍을 향할 때 => 이동거리가 짧은 게 빠지도록 함

    # 어디로 이동할 건지 direction
    dx, dy = dirs

    # 각 구슬의 y좌표, x좌표
    rx, ry = start_r
    bx, by = start_b

    # 정지하기까지 이동한 횟수 => 같은 위치에 있을 때 선후 관계를 가리는 용도
    r_cnt, b_cnt = 0, 0

    # 구슬이 빠져나갔는지 여부
    r_out, b_out = False, False

    # 빨간 공
    nx, ny = rx + dx, ry + dy
    while 0 <= nx < n and 0 <= ny < m:
        r_cnt += 1
        # 구슬이 밖으로 빠져나옴
        if maps[ny][nx] == 'O':
            r_out = True
            break
        # 움직일 수 없음
        elif maps[ny][nx] == '#':
            start_r = (rx, ry)
            r_cnt -= 1
            break
        # 이동 가능
        elif maps[ny][nx] == '.':
            rx, ry = nx, ny
            nx, ny = rx + dx, ry + dy

    # 파란 공
    nx, ny = bx + dx, by + dy
    while 0 <= nx < n and 0 <= ny < m:
        b_cnt += 1
        if maps[nx][ny] == 'O':
            b_out = True
            break
        elif maps[ny][nx] == '#':
            start_b = (by, bx)
            b_cnt -= 1
            break
        elif maps[ny][nx] == '.':
            bx, by = nx, ny
            nx, ny = bx + dx, by + dy

    # 두 개가 같은 위치에 겹친 경우
    if start_r == start_b:
        # r이 더 오래 걸렸으면 r을 한 칸 뒤로 보내기
        if r_cnt > b_cnt:
            start_r = (rx - dx, ry - dy)
        # b가 더 오래 걸렸으면 b를 한 칸 뒤로 보내기
        else:
            start_b = (bx - dx, by- dy)

    # 실패
    # b가 통과한 경우
    if b_out:
        return
    # 둘다 움직이지 않는 경우
    elif r_cnt == b_cnt == 0:
        return
    # 성공: r만 통과하고 b는 통과하지 못한 경우
    elif r_out and not b_out:
        mins = min(mins, cnt)
        return
    else:
        bfs(maps, start_r, start_b, (0, 1), cnt + 1)
        bfs(maps, start_r, start_b, (1, 0), cnt + 1)
        bfs(maps, start_r, start_b, (0, -1), cnt + 1)
        bfs(maps, start_r, start_b, (-1, 0), cnt + 1)


input = sys.stdin.readline
n, m = map(int, input().split()) # 세로, 가로
maps = [list(input().strip()) for _ in range(n)]
for i in range(n):
    for j in range(m):
        if maps[i][j] == 'R':
            r = (i, j)
        if maps[i][j] == 'B':
            b = (i, j)

mins = float('inf')

dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for head in dirs:
    bfs(maps, r, b, head, 1)

if mins == float('inf'):
    print(-1)
else:
    print(mins)

