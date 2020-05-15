# 사람이 계단 선택하는 경우의 수만큼
# 사람-계단 거리
def my_gen(people, stair):
    for i in range(1 << len(people)):
        g1 = [] # 집합 내 사람 - 계단1 거리 => 시간
        g2 = [] # 집합 내 사람 - 계단2 거리 => 시간
        for j in range(len(people)): # 거리두기
            if i & (1 << j):
                dis = abs(people[j][0] - stair[0][0]) + abs(people[j][1] - stair[0][1])
                g1.append(dis)
            else:
                dis = abs(people[j][0] - stair[1][0]) + abs(people[j][1] - stair[1][1])
                g2.append(dis)
        yield sorted(g1), sorted(g2)

# memoization
memo = {}
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    Map = [list(map(int, input().split()))]

    # 사람, 계단 찾기
    people = []
    stair = []
    for i in range(N):
        for j in range(N):
            if Map[i][j]:
                if Map[i][j] == 1:
                    people.append((i, j))
                else:
                    stair.append((i, j))

    result = float('inf')
    for g1, g2 in my_gen(people, stair):
        t1 = t2 = 0
        s1 = []
        s2 = []
        # memoization
        m1 = (g1, stair[0][2])
        m2 = (g2, stair[1][2])

        # 1번 계단
        if m1 in memo:
            t1 = memo[m1]
        else:
            while g1 or s1:
                t1 += 1 # 시간 흐름
                if g1 or s1:
                    # 계단까지 이동(3명)
                    i = 0
                    for _ in range(min(len(s1), 3)):
                        if s1[i]:
                            i += 1
                        else:
                            s1.pop(i)

                    # 입구에 도착한 사람 계단으로 이동
                    while g1 and t1 == g1[0]:
                        g1.pop(0)
                        s1.append

