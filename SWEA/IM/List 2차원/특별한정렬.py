T = int(input())

for tc in range(1, T+1):
    N = int(input())
    a = sorted(list(map(int, input().split())))

    print('#{}'.format(tc), end=" ")
    for _ in range(5):
        print('{}'.format(a.pop()), end=" ")
        print('{}'.format(a.pop(0)), end=" ")
    print()