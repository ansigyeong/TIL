from pprint import pprint

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    paper = [[0 for _ in range(10)] for _ in range(10)]

    # 1: 빨, 2: 파
    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                paper[r][c] += color

    # pprint(paper)
    cnt = 0
    for i in range(len(paper)):
        for j in range(len(paper)):
            if paper[i][j] == 3:
                cnt += 1

    print('#{} {}'.format(tc, cnt))