def vlqhskcl(num):

    list = [1, 1]

    if int(num) == 1:
        list = [1]

    if int(num) > 2:
        for i in range(int(num)):
            temp = list[i] + list[i+1]
            list.append(temp)
            temp = 0

    return print(list)

vlqhskcl(10)
