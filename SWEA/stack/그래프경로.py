def dfs(S):
    global flag, V, G
    if S == G:
        flag = 1
        return
    visited[S] = 1

    for i in range(1, V+1):
        if adj[S][i] == 1 and visited[i] == 0:
            dfs(i)

T = int(input())

for tc in range(1, T+1):
    flag = 0
    V, E = map(int, input().split())
    adj = [[0 for _ in range(V+1)] for _ in range(V+1)]
    visited = [0 for _ in range(V+1)]
    for _ in range(E):
        s, g = map(int, input().split())
        adj[s][g] = 1
    S, G = map(int, input().split())

    dfs(S)

    print('#{} {}'.format(tc, flag))

    

    