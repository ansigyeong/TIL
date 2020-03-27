def find(n, i, j):
    global N, cnt, maxCnt, m, minM
    if i == N and j == N:
        return
    else:
        di = [0, 0, -1, 1, -1, -1, 1, 1]
        dj = [-1, 1, 0, 0, -1, 1, -1, 1]
        for k in range(8):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N and data[ni][nj] == n:
                cnt += n
                m += 1
                find(n, ni, nj)

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    maxCnt = 0 # 최대 매장량
    minM = 0 # 최대 매장량일때의 면적

    for i in range(N):
        cnt = 0 # 매장량
        m = 0 # 광맥 면적
        for j in range(N):
            if data[i][j] == 0: # 값이 0일 때 continue
                continue
            else: # 값이 0이 아닐 때 함수 호출하여 연산 시작
                n = data[i][j]
                find(n, i, j)

    print('#{} {} {}'.format(tc, maxCnt, minM))