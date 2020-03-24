T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    cnt = 0
    for i in range(1<<len(A)):
        temp = []
        for j in range(len(A)):
            if i & 1<<j:
                temp.append(A[j])

        if len(temp) == N and sum(temp) == K:
            cnt += 1

    print('#{} {}'.format(tc, cnt))