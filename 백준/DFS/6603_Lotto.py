import sys
from itertools import combinations
read = lambda : sys.stdin.readline().strip().split()

while True:
    lst = list(map(int, read()))
    n = lst.pop(0)
    if len(lst) == 0:
        break
    else:
        for c1, c2, c3, c4, c5, c6 in combinations(lst, 6):
            print('{} {} {} {} {} {}'.format(c1, c2, c3, c4, c5, c6))
        print()