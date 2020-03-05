def paper(N):
    result = [0, 1, 3]
    for i in range(3, N//10 + 1):
        result.append(2 * result[i - 2] + result[i - 1])
    return result[-1]

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    print('#{} {}'.format(tc, paper(N)))
