T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    busStop = list(map(int, input().split()))
    move = 0
    charge = 0

    while move <= N:
        move += K
        if move >= N:
            break
        if move not in busStop:
            cnt = 0
            while move not in busStop:
                move -= 1
                cnt += 1
            if cnt == K:
                charge = 0
                break
            charge += 1

        elif move in busStop:
            charge += 1

    print('#{} {}'.format(tc, charge))