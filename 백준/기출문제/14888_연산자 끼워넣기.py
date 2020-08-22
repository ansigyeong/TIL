import sys


def calculate(number, index, add, subtract, multiple, division):
    global N, max_value, min_value
    if index == N:
        max_value = max(number, max_value)
        min_value = min(number, min_value)
        return
    else:
        if add:
            calculate(number + numbers[index], index + 1, add - 1, subtract, multiple, division)
        if subtract:
            calculate(number - numbers[index], index + 1, add, subtract - 1, multiple, division)
        if multiple:
            calculate(number * numbers[index], index + 1, add, subtract, multiple - 1, division)
        if division:
            calculate(int(number / numbers[index]), index + 1, add, subtract, multiple, division - 1)

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
add, subtract, multiple, division = map(int, sys.stdin.readline().split())

max_value = float('-inf')
min_value = float('inf')

calculate(numbers[0], 1, add, subtract, multiple, division)

print(max_value)
print(min_value)