def solution():
    cnt = 0

    for i in range(N):
        if A[i] > 0:
            A[i] -= Master
            cnt += 1

        if A[i] > 0:
            cnt += int(A[i] / Sub)
            if A[i] % Sub != 0:
                cnt += 1

    return cnt

import sys

N = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))

Master, Sub = map(int, sys.stdin.readline().split())

print(solution())