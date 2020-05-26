# 5차시

data = []
temp = []

for i in range(2, 10):
    for j in range(1, 10):
        if (i*j) % 3 != 0 and (i*j) % 7 != 0:
            temp.append(i*j)
    data.append(temp)
    temp = []

print(data)