T = int(input())

for tc in range(1, T+1):
    N = int(input()) # 이동시간
    A = list(map(int, input().split())) # 10개의 정수
    for _ in range(N): # 이동시간 N만큼 연산 반복함
        temp = [0] * len(A) # N에 따라 달라지는 요소를 저장할 임시 배열(배열 A는 영향을 받지 않은 채로 연산해야 함)
        for i in range(len(A)):
            if A[i] >= 10 or A[i] <= -10: ### 절대값이 10 이상인 경우에 대한 연산
                if i-1 < 0: # 인덱스가 범위를 벗어나는 경우
                    temp[i] = abs(A[i])//2
                    temp[i+1] = abs(A[i])//2
                if i+1 >= len(A): # 인덱스가 범위를 벗어나는 경우
                    temp[i] += -abs(A[i])//2
                    temp[i-1] += -abs(A[i])//2
                else: # 인덱스가 범위 내에 있는 경우
                    temp[i-1] += -abs(A[i])//2
                    temp[i+1] = abs(A[i])//2
            else: ### 절대값이 10 미만인 경우에 대해 연산
                if A[i] > 0: # 값이 양수일 때 오른쪽으로 이동함
                    if 0 <= i + 1 < len(A):
                        temp[i+1] = A[i]
                    else:
                        temp[i] += -A[i]
                elif A[i] < 0: # 값이 음수일 때 왼쪽으로 이동함
                    if 0 <= i-1 < len(A):
                        temp[i-1] += A[i]
                    else:
                        temp[i] += -A[i]
                elif A[i] == 0: # 값이 0일 때 continue
                    continue
        A = temp # A를 temp로 변경한 후 연산 반복


    print('#{}'.format(tc), end=" ")
    for k in A:
        print('{}'.format(k), end=" ")
    print()