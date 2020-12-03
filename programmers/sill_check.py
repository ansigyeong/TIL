array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
answer = []
for command in commands:
    temp = []
    first_idx = array[command[0]-1]
    last_idx = array[command[1]-1]
    if first_idx == last_idx:
        answer.append(command[2])
    else:
        
        for i in range(first_idx, last_idx):
            temp.append(array[i])
            temp.sort()
            print(temp)
    # result = temp[command[2]]
    # answer.append(result)
    # print(answer)