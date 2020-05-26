# 6차시

import sys
sys.stdin = open("2_4.txt")

data = []

for _ in range(5):
    data.append(int(input()))

ave = sum(data) / 5

print('입력된 값 {}의 평균은 {}입니다.'.format(data, ave))