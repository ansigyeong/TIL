from collections import deque

N = int(input())

data = map(int, input().split())
data_list = []
for idx, value in enumerate(data):
    data_list.append((idx + 1, value))

visit = [0 for _ in range(N)]

answer = []
now = 0
for _ in range(N):
    idx, step = data_list[now]
    answer.append(idx)
    visit[idx - 1] = 1
    while step != 0 and len(answer) != N:
        if step > 0:
            now += 1
            now %= N
        else:
            now -= 1
            now = -(abs(now) % N)
        if visit[now]:
            continue
        if step > 0:
            step -= 1
        else:
            step += 1
    visit[now] = 1

print(*answer)