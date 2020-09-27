import sys


def find_percent(n, k, s):
    global max_percent

    if n == k:
        if max_percent < s*100:
            max_percent = s*100
    elif max_percent >= s*100:
        return
    else:
        for i in range(k):
            if U[i] == 0:
                U[i] = 1 # i번 사람이 n번 일을 맡음
                find_percent(n+1, k, s*P[i][n]/100) # n번까지의 성공 확률을 계산함
                U[i] = 0 # 다른 일을 맡도록 함


T = int(sys.stdin.readline())

for tc in range(1, T+1):
    N = int(sys.stdin.readline())
    P = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    U = [0] * N
    max_percent = 0

    find_percent(0, N, 1)

    # 모든 일을 성공할 확률이 최대화될 때의 확률을 퍼센트 단위로 소수점 아래 7번째 자리에서 반올림하여 6번째까지 출력한다.

    print('#{} {:.6f}'.format(tc, max_percent))