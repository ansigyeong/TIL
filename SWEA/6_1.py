import sys
sys.stdin = open("6_1.txt", "r")

a=int(input())
divisor = []

for i in range(1, a+1):
    if a % i == 0:
        divisor.append(i)
        
for j in range(len(divisor)):
    print('{}(은)는 {}의 약수입니다.'.format(divisor[j], a))
        