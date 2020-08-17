def clean():
    pass

import sys


N, M = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split()) # d => 0북 1동 2남 3서
area = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

visited = 0

clean()

print(visited)