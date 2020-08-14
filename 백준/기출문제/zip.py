def rotate(shape):
    return [list(reversed(i)) for i in list(map(list, zip(*shape)))]


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

print(rotate(shape1))

print(rotate(shape2))

print(rotate(shape3))

print(rotate(shape4))

print(rotate(shape5))