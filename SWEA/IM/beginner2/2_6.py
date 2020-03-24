# 7차시

N = int(input())

data = []

for i in range(1, N+1):
    if N % i == 0:
        data.append(i)

print(data)