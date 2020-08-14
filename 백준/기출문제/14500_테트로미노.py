def check_shape(arr, shape):
    global max_sum
    y_length = len(arr) - len(shape)
    x_length = len(arr[0]) - len(shape[0])
    for start_y in range(y_length + 1):
        for start_x in range(x_length + 1):
            # 좌표 처음부터 순회
            value = 0
            for y in range(len(shape)):
                for x in range(len(shape[0])):
                    if shape[y][x] == 1:
                        value += arr[start_y + y][start_x + x]
            max_sum = max(max_sum, value)

def rotate(shape):
    return [list(reversed(i)) for i in list(map(list, zip(*shape)))]

import sys
# 4개 => 테트로미노
N, M = map(int, sys.stdin.readline().split()) # 세로, 가로
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
max_sum = 0

line = [[1], [1], [1], [1]]
box = [
    [1, 1],
    [1, 1]
]
shape1 = [
    [1, 0],
    [1, 0],
    [1, 1]
]
shape2 = [
    [1, 0],
    [1, 1],
    [0, 1]
]
shape3 = [
    [1, 1, 1],
    [0, 1, 0]
]
shape4 = [
    [0, 1],
    [0, 1],
    [1, 1]
]
shape5 = [
    [0, 1],
    [1, 1],
    [1, 0]
]
shape_list = [line, box, shape1, shape2, shape3, shape4, shape5]

for shape in shape_list:
    if shape == line:
        for _ in range(2):
            check_shape(arr, shape)
            shape = rotate(shape)
    elif shape == box:
        check_shape(arr, shape)
    else:
        for _ in range(4):
            check_shape(arr, shape)
            shape = rotate(shape)

print(max_sum)