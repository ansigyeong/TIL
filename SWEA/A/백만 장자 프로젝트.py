T = int(input())

for tc in range(1, T+1):
    N = int(input())
    selling_price = list(map(int, input().split()))

    for i in range(N-1):
        if selling_price[i] < selling_price[i+1]:
            k = selling_price[i+1]
