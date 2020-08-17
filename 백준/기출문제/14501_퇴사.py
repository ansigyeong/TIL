# 1회독 => DP

# 이 문제는 완전탐색을 할 때 최악의 경우 매일 상담을 해야함
# 그래도 N의 범위가 15이하이므로 2^15(32768)번만 작업하면 되므로 완전탐색을 해도 무방하다.

# Brute Force
N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]
max_ = 0


def func(day, pay):
    global max_
    if day >= N:
        if day == N:
            tot = sum(pay)
        else:
            tot = sum(pay[:-1])

        if tot > max_:
            max_ = tot
        return

    # 해당 날짜에 상담 X
    func(day + 1, pay)

    # 해당 날짜에 상담 O
    nday, npay = day + table[day][0], pay + [table[day][1]]
    func(nday, npay)


func(0, [])
print(max_)

# 이 문제는 시간 복잡도가 O(2^N)이므로 N이 커질수록 시간 복잡도는 기하급수적으로 커짐
# 이때는 DP로 문제를 해결함

# Dynamic Programming
N = int(input())
schedules = list(list(map(int, input().split())) for _ in range(N))
dp = [0] * N

for i in range(N):
    if i + schedules[i][0] <= N:
        dp[i] = schedules[i][1]
        for j in range(i):
            if j + schedules[j][0] <= i:
                dp[i] = max(dp[i], dp[j] + schedules[i][1])

print(max(dp))

