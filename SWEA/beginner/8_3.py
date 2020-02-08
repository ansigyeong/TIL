def thtn(num):
    cnt = 0
    for i in range(1, int(num) + 1):
        if num % i == 0:
            cnt += 1
    if cnt == 2:
        return print('소수입니다.')
    else:
        return print('소수가 아닙니다.')


thtn(13)