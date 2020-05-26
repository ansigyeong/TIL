import sys
sys.setrecursionlimit(10**8)

def dfs(i):
    visited[i] = 1
    for j in range(1, n+1):
        if adj[i][j] == 1 and not visited[j]:
            dfs(j)


read = lambda : sys.stdin.readline().strip().split()
n, m = map(int, read())
adj = [[0 for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, read())
    adj[u][v] = adj[v][u] = 1
visited = [0] * (n + 1)
count = 0

for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)
        count += 1

print(count)