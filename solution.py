import sys

N = int(sys.stdin.readline())
schedules = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [0] * N

for i in range(N):
    if i + schedules[i][0] <= N:
        dp[i] = schedules[i][1]
        for j in range(i):
            if j + schedules[j][0] <= i:
                dp[i] = max(dp[i], dp[j] + schedules[i][1])

print(max(dp))
