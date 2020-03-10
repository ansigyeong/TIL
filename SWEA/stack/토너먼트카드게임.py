T = int(input())

for tc in range(1, T+1):
    # 1 가위 2 바위 3 보
    # 같은 카드인 경우 번호가 작은 쪽을 승자로 함
    N = int(input())
    card = [0]
    card += [int(x) for x in input().split()]

    stack1 = []
    stack2 = []

    n = 1+N // 2

    for i in range(1, n-1):
        if i % 2 != 0:
            if card[i] == 1:
                if card[i+1] == 1:
                    lst = [i, card[i]]
                    stack1.append(lst)
                elif card[i+1] == 2:
                    lst = [i + 1, card[i+1]]
                    stack1.append(lst)
                elif card[i+1] == 3:
                    lst = [i, card[i]]
                    stack1.append(lst)

            elif card[i] == 2:
                if card[i + 1] == 1:
                    lst = [i, card[i]]
                    stack1.append(lst)
                elif card[i + 1] == 2:
                    lst = [i, card[i]]
                    stack1.append(lst)
                elif card[i + 1] == 3:
                    lst = [i + 1, card[i+1]]
                    stack1.append(lst)

            elif card[i] == 3:
                if card[i + 1] == 1:
                    lst = [i + 1, card[i + 1]]
                    stack1.append(lst)
                elif card[i + 1] == 2:
                    lst = [i, card[i]]
                    stack1.append(lst)
                elif card[i + 1] == 3:
                    lst = [i, card[i]]
                    stack1.append(lst)

        else:
            continue

    for i in range(n-1, N-1):
        if i % 2 != 0:
            if card[i] == 1:
                if card[i+1] == 1:
                    lst = [i, card[i]]
                    stack2.append(lst)
                elif card[i+1] == 2:
                    lst = [i + 1, card[i+1]]
                    stack2.append(lst)
                elif card[i+1] == 3:
                    lst = [i, card[i]]
                    stack2.append(lst)

            elif card[i] == 2:
                if card[i + 1] == 1:
                    lst = [i, card[i]]
                    stack2.append(lst)
                elif card[i + 1] == 2:
                    lst = [i, card[i]]
                    stack2.append(lst)
                elif card[i + 1] == 3:
                    lst = [i + 1, card[i+1]]
                    stack2.append(lst)

            elif card[i] == 3:
                if card[i + 1] == 1:
                    lst = [i + 1, card[i + 1]]
                    stack2.append(lst)
                elif card[i + 1] == 2:
                    lst = [i, card[i]]
                    stack2.append(lst)
                elif card[i + 1] == 3:
                    lst = [i, card[i]]
                    stack2.append(lst)

        else:
            continue

    while