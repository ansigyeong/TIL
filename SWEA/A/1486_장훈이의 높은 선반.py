from itertools import combinations

def solve(H):
    global N, B, min_height
    for i in range(1, N+1):
        temp_list = list(combinations(H, i))
        for temp in temp_list:
            temp_height = sum(temp)
            if temp_height >= B and temp_height <= min_height:
                min_height = temp_height
    return


T = int(input())

for tc in range(1, T+1):
    N, B = map(int, input().split()) # N명의 점원, 선반의 높이 B
    H = list(map(int, input().split()))
    min_height = float('inf')
    solve(H)
    result = abs(B - min_height)
    print('#{} {}'.format(tc, result))