n, m = map(int, input().split(', '))

data = [[ 0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        data[i][j] = i*j

print(data)
