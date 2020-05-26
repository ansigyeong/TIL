import sys
from pprint import pprint


def dfs(start):
    for end in range(n+1):
        if adj[start][end] == 1:
            result[start][end] = 1
            




read = lambda : sys.stdin.readline().strip().split()
n = int(read().pop())
adj = [list(map(int, read())) for _ in range(n)]
result = [[0 for _ in range(n)] for _ in range(n)]
visited = [0 for _ in range(n)]

for i in range(n):
    if visited[i] == 0:
        dfs(i, j)
        visited[i] = 1

print(result)