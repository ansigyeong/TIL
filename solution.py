def bfs(start):
    visited = [start]
    queue = [start]
    while queue:
        k = queue.pop(0)
        for c in range(n+1):
            if matrix[k][c] == 1 and c not in visited:
                visited.append(c)
                queue.append(c)
    return visited

def dfs(start, visited):
    visited += [start]
    for c in range(n+1):
        if matrix[start][c] == 1 and (c not in visited):
            dfs(c, visited)
    return visited


n, m, v = map(int, input().split()) #  정점의 개수, 간선의 개수, 탐색을 시작할 정점의 번호
matrix = [[0 for _ in range(n+1)] for _ in range(n+1)]
stack = []
for _ in range(m):
    i, j = map(int, input().split())
    matrix[i][j] = matrix[j][i] = 1


print(*dfs(v, []))
print(*bfs(v))