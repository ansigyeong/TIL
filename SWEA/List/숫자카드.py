T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input()))
    numDict = {}

    for i in numbers:
        if i not in numDict:
            numDict[i] = 1
        else:
            numDict[i] += 1

    result1 = []
    for key, value in numDict.items():
        if value == max(numDict.values()):
            result1.append(key)
            result2 = value

    print('#{} {} {}'.format(tc, max(result1), result2))