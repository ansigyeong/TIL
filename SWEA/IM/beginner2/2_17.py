import math

data = []
data = list(map(int, input().split(', ')))

for i in range(len(data)):
    data[i] = data[i] * 2 * math.pi

    if i == len(data) - 1:
        print('%0.2f' %data[i])

    else:
        print('%0.2f' %data[i], end=", ")