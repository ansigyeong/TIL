T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    result = []

    for i in range(N-M+1):
        temp = 0
        for j in range(M):
            temp += data[i+j]
        result.append(temp)

    print('#{} {}'.format(tc, max(result)-min(result)))