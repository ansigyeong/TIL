targets = ['W', 'B', 'R']

def dfs(idx, color, temp_value):
    global result

    # 가지치기
    if result <= temp_value:
        return

    # 결과 더하기
    if idx == N - 1:
        result = temp_value
        return

    # 인덱스 떄문에 최댓값은 3으로 설정함
    for i in range(color, min(3, color + 2)):
        temp = 0
        # 마지막줄까지 왔는데 컬러가 흰색이면 다음으로 넘어가기
        if idx >= N-2 and i == 0:
            continue
        for j in flag[idx]:
            # 색상이 다른 것들 카운트
            if j != targets[i]:
                temp += 1
        dfs(idx + 1, i, temp_value + temp)


def init():
    global result
    for i in flag[0]:
        if i != 'W':
            result += 1
    for i in flag[N-1]:
        if i != 'R':
            result += 1

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    flag = [list(input()) for _ in range(N)]

    # 최종 결과값
    result = float('inf')

    # 개수 체크하기
    dfs(1, 0, 0)

    # 제일 위와 아래 체크하기
    init()

    print('#{} {}'.format(tc + 1, result))

