from itertools import permutations, combinations, product
import copy


items = ['사과', '배', '바나나', '복숭아', '포도']

# 1. permutation => 순열
# => from itertools import permutations
print('순열')
print(list(permutations(items, 2)))

# 2. combination => 조합

# 2-1. 하나의 리스트에서 모든 조합 계산
# => from itertools import combinations
print('하나의 리스트에서 모든 조합 계산')
print(list(combinations(items, 2)))

# 2-2. 두 개 이상의 리스트에서 모든 조합 계산
# => from itertools import product
print('두 개 이상의 리스트에서 모든 조합 계산')
print(list(product(*items)))

# 2-3. 2차원 배열에서의 조합
# itertools
arr = [[0, 1], [2, 3], [4, 5]]
def itertoolsSetOne():
    posList = []

    # 모든 원소를 담은 리스트를 생성
    for i in range(0, 3*2):
        posList.append((i//2, i % 2))
        # 숫자를 0 ~ n*m 까지 증가시킬때 (i/m, i%m)을 좌표로 하면
        # 2차원 배열의 모든 인덱스를 탐색할 수 있음


    # itertools를 활용하여 조합 구하기
    print('itertools로 2차원 배열에서 조합 구하기')
    for pos1, pos2, pos3 in combinations(posList, 3):
        temp = copy.deepcopy(arr)
        temp[pos1[0]][pos1[1]] = 1
        temp[pos2[0]][pos2[1]] = 1
        temp[pos1[0]][pos2[1]] = 1

        for j in range(0, 3):
            print(temp[j])
        print('\n')

# 재귀
def recursionSetOne(start, count):
    # 원소를 모두 골랐을 경우 출력
    if count == 0:
        print('재귀로 2차원 배열 조합 구하기')
        for j in range(0, 3):
            print(arr[j])
        print('\n')
        return

    # n번째 원소부터 원소를 선택
    # n * m
    for i in range(start, 3*2):
        x = i // 2
        y = i % 2

        # 원소 선택
        arr[x][y] = 1

        # 나머지 배열의 원소들 중에서 count - 1만큼을 선택
        recursionSetOne(i + 1, count - 1)

        # 선택한 원소를 초기화
        arr[x][y] = 0


if __name__ == "__main__":
    # 2차원 배열 arr에서 2가지 원소를 선택하여 1을 삽입하는 조합
    # start: 0, 개수: n
    recursionSetOne(0, 3)
    itertoolsSetOne()

    # output

    # [1, 1]
    # [1, 0]

    # [1, 1]
    # [0, 1]