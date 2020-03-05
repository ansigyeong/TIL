T = int(input())

for tc in range(1, T+1):
    test = input()
    list = []
    for i in test:
        if len(list) == 0:
            list.append(i)
        else:
            if list[-1] == i:
                list.pop()
            else:
                list.append(i)

    print('#{} {}'.format(tc, len(list)))