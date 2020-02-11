N = int(input())

list = []

while N // 2:
    a = N % 2 
    list.append(str(a))
    N //= 2
    if N == 1:
        list.append(str(N))

print(''.join(list))