import sys
from pprint import pprint


read = lambda : sys.stdin.readline().strip().split()
n = int(read().pop())
adj = [list(map(int, read())) for _ in range(n)]

# 플로이드 위셜 알고리즘(Floyd Warshall Algorithm) 이용
for k in range(n):
    for i in range(n):
        for j in range(n):
            if adj[i][k] and adj[k][j]:
                adj[i][j] = 1

for i in range(n):
    for j in range(n):
        print(adj[i][j], end=" ")
    print()