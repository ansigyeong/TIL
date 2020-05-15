N, M, V = map(int, input().split())
adj = [[0 for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M):
    i, j = map(int, input().split())
    adj[i][j] = adj[j][i] = 1

def dfs(current, stack):
    stack += [current]
    for search in range(len(adj[current])):
        if adj[current][search] and search not in stack:
            dfs(search, stack)
    return stack

def bfs(start):
    queue = [start]
    stack = [start]
    while queue:
        current = queue.pop(0)
        for search in range(len(adj[current])):
            if adj[current][search] and search not in stack:
                queue += [search]
                stack += [search]
    return stack

print(*dfs(V, []))
print(*bfs(V))