N = int(input())

for n in range(1, N+1):
    m = str(n)
    cnt = 0
    if '3' in m or '6' in m or '9' in m:
        cnt = m.count('3') + m.count('6') + m.count('9')
        j = '-' * cnt
        print('{}'.format(j), end=" ")
    else:
        print('{}'.format(m), end=" ")