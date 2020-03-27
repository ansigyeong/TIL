N = int(input())
P = list(map(int, input().split()))

P.sort()

# print(P)
sum = 0

for i in range(N):
    k = 0
    temp = 0
    while True:
        temp += P[k]
        if k == i:
            break
        else:
            k += 1
    sum += temp

print(sum)
