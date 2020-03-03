T = int(input())

for tc in range(1, T+1):
    P, A, B = map(int, input().split())

    # A
    l = 1
    r = P
    c = int((l + r) / 2)
    cntA = 0
    while c != A:
        if c == A:
            cntA += 1
            break
        if c < A:
            l = c
            c = int((l + r) / 2)
            cntA += 1
        if c > A:
            r = c
            c = int((l + r) / 2)
            cntA += 1

    # B
    l = 1
    r = P
    c = int((l + r) / 2)
    cntB = 0
    while c != B:
        if c == B:
            cntB += 1
            break
        if c < B:
            l = c
            c = int((l + r) / 2)
            cntB += 1
        if c > B:
            r = c
            c = int((l + r) / 2)
            cntB += 1

    if cntA > cntB:
        result = 'B'
    elif cntA < cntB:
        result = 'A'
    else:
        result = 0

    print('#{} {}'.format(tc, result))
