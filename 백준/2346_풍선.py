N = int(input())

input_data = list(map(int, input().split()))
balloon_data = []

for idx, value in enumerate(input_data):
    balloon_data.append((idx+1), value)

visit = [0 * N]

answer = []
now = 0

for _ in range(N):
    idx, step = balloon_data[now]
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