data = [2, 4, 6, 8, 10]

def my_func(n):
    data = [2, 4, 6, 8, 10]
    if n in data:
        return True
    if n not in data:
        return False

print(data)
x = 5
print('{} => {}'.format(x, my_func(x)))
y = 10
print('{} => {}'.format(y, my_func(y)))