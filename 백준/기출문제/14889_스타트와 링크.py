import sys
import itertools


def bruteforce(S, N):
    global min_result
    cnt = N // 2
    members = set(range(N))
    teams = itertools.combinations(members, cnt)

    for team in teams:
        group1 = set(team)
        group2 = list(members - group1)
        group1_ability = 0
        group2_ability = 0

        # members = list(members)
        # group1 = list(group1)

        # devide in half by containing 0 or not(0을 포함하거나 포함하지 않고 반으로 나눔)
        if team[0] != 0:
            break

        # itertools return result by the generator object
        group1_persons = itertools.combinations(group1, 2)
        for persons in group1_persons:
            group1_ability += S[persons[0]][persons[1]]

        group2_persons = itertools.combinations(group2, 2)
        for persons in group2_persons:
            group2_ability += S[persons[0]][persons[1]]

        if abs(group2_ability - group1_ability) < min_result:
            min_result = abs(group2_ability - group1_ability)

    return min_result



N = int(sys.stdin.readline())
S = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

min_result = float('inf')

for i in range(N):
    for j in range(N):
        if j > i:
            S[i][j] = S[i][j] + S[j][i]
            S[j][i] = 0

print(bruteforce(S, N))

