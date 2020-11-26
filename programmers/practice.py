def solution(n, arr1, arr2):
    temp = []
    for i in range(n):
        # print(bin(arr1[i] | arr2[i]))
        temp.append(bin(arr1[i] | arr2[i])[2:]
        .zfill(n)
        .replace('1', '#')
        .replace('0', ' '))
    print(temp)
        
solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])