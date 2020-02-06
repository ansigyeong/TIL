import sys
sys.stdin = open("6_2.txt", "r")

N = int(input())
divisor = []

for i in range(1, N+1):
    if N % i == 0:
        divisor.append(i)

for j in range(len(divisor)):
    print('{}(은)는 {}의 약수입니다.'.format(divisor[j], N))
if len(divisor) == 2:
    print('{}(은)는 1과 {}로만 나눌 수 있는 소수입니다.'.format(N, N))
    
