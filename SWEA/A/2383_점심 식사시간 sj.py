# 사람이 계단을 선택하는 경우의 수만큼
# 계단까지의 거리를 반환하는 제네레이터
def my_gen(people, stair):
    for i in range(1 << len(people)):
        g1 = []
        g2 = []
        for j in range(len(people)):
            if i & (1 << j):
                dist = abs(people[j][0] - stair[0][0]) + abs(people[j][1] - stair[0][1])
                g1.append(dist)
            else:
                dist = abs(people[j][0] - stair[1][0]) + abs(people[j][1] - stair[1][1])
                g2.append(dist)
        yield sorted(g1), sorted(g2)


# 메모이제이션
memo = {}
T = int(input())
for test_case in range(1, 1 + T):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]

    # 사람과 계단 찾기
    people = []
    stair = []
    for r in range(N):
        for c in range(N):
            if MAP[r][c]:
                if MAP[r][c] == 1:
                    people.append((r, c))
                else:
                    stair.append((r, c, MAP[r][c]))

    result = float('inf')
    for g1, g2 in my_gen(people, stair):
        t1 = t2 = 0
        s1 = []
        s2 = []
        # 메모이제이션
        m1, m2 = (tuple(g1), stair[0][2]), (tuple(g2), stair[1][2])

        # 1번 계단
        if m1 in memo:
            t1 = memo[m1]
        else:
            while g1 or s1:
                # 시간 흐름
                t1 += 1
                if g1 or s1:
                    # 계단 이동 완료 (3명 까지)
                    i = 0
                    for _ in range(min(len(s1), 3)):
                        if s1[i]:
                            i += 1
                        else:
                            s1.pop(i)
                    # 계단 내려가기 (3명 까지)
                    i = 0
                    for _ in range(min(len(s1), 3)):
                        s1[i] -= 1
                        i += 1

                    # 입구에 도착한 사람 계단으로
                    while g1 and t1 == g1[0]:
                        g1.pop(0)
                        s1.append(stair[0][2])
            # 결과 메모
            memo[m1] = t1

        # 2번 계단
        if m2 in memo:
            t2 = memo[m2]
        else:
            while g2 or s2:
                # 시간 흐름
                t2 += 1
                if g2 or s2:
                    # 계단 이동 완료 (3명 까지)
                    i = 0
                    for _ in range(min(len(s2), 3)):
                        if s2[i]:
                            i += 1
                        else:
                            s2.pop(i)
                    # 계단 내려가기 (3명 까지)
                    i = 0
                    for _ in range(min(len(s2), 3)):
                        s2[i] -= 1
                        i += 1

                    # 입구에 도착한 사람 계단으로
                    while g2 and t2 == g2[0]:
                        g2.pop(0)
                        s2.append(stair[1][2])
            # 결과 메모
            memo[m2] = t2

        sub_res = max(t1, t2)  # 늦게 끝난 계단
        if sub_res < result:  # 최소값
            result = sub_res

    print('#{} {}'.format(test_case, result))