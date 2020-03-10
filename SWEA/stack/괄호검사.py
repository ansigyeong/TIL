import sys
sys.stdin = open('괄호검사.txt')

T = int(input())

for tc in range(1, T+1):
    test = input()
    temp = []
    result = 1

    for i in test:
        if i == '(' or i == '{':
            temp.append(i)
        elif i == ')' or i == '}':
            if len(temp) == 0:
                result = 0
                break
            else:
                a = temp.pop()
                if i == ')' and a == '{':
                    result = 0
                    break
                elif i == '}' and a == '(':
                    result = 0
                    break
    if len(temp) != 0:
        result = 0

    print('#{} {}'.format(tc, result))


