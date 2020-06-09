from copy import deepcopy

def findSafeArea(height):
    copyArr = deepcopy(arr)
    for i in range(n):
        for j in range(n):
            if arr[i][j] <= height:
                copyArr[i][j] = 0
    checkSafeNumber()

def checkSafeNumber():
    global copyArr
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    for i in range(n):
        for j in range(n):
            if copyArr
    for k in range(4):


import sys
read = lambda : sys.stdin.readline().strip().split()

n = int(read()) # 2 이상 100 이하 정수
arr = [[int(i) for i in read()] for _ in range(n)] # 1 이상 100 이하 정수

max_safe_area = 0

for i in range(100):
    findSafeArea(i)

print(max_safe_area)
