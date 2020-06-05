def findSafeArea(height):
    pass

import sys
read = lambda : sys.stdin.readline().strip().split()

n = int(read())
arr = [[int(i) for i in read()] for _ in range(n)]

max_safe_area = 0

for i in range(100):
    findSafeArea(i)

print(max_safe_area)
