list = [3, 5, 4, 1, 8, 10, 2]


def max_return(*args):
    max_num = 0
    for i in args:
        if i > max_num:
            max_num = i
    return max_num


for i in list:
    result = max_return(i)


print('max({}) => {}'.format(', '.join(map(str, list)), result))