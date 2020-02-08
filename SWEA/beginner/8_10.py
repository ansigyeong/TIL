def countdown(n):
    if int(n) <= 0:
        print('카운트다운을 하려면 0보다 큰 입력이 필요합니다.')
    if int(n) > 0:
        for i in range(int(n), 0, -1):
            print(i)

countdown(0)
countdown(10)
