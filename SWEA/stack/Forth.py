T = int(input())

for tc in range(1, T+1):
    code = input().split()
    stack = []

    for i in code:
        if i.isdecimal():
            stack.append(int(i))
        elif i == '.':
            if len(stack) != 1:
                result = 'error'
                break
            else:
                result = stack.pop()
                break
        else:
            if len(stack) < 2:
                result = 'error'
                break
            m = stack.pop()
            n = stack.pop()
            if i == '+':
                stack.append(n + m)
            elif i == '-':
                stack.append(n - m)
            elif i == '*':
                stack.append(n * m)
            elif i == '/':
                stack.append(n // m)

    print('#{} {}'.format(tc, result))