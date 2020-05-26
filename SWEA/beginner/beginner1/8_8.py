n, m = map(int, input().split(', '))


def my_square(k):
    result = k ** 2

    return result


print('square({}) => {}'.format(n, my_square(n)))
print('square({}) => {}'.format(m, my_square(m)))