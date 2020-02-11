a = []

for i in range(200, 301):
    if i % 2 == 0 and (i//10) % 2 == 0 and (i//100) % 2 ==0:
        a.append(str(i))

#print(a)
print('{}'.format(','.join(a)))

"""
초기 코드
list = []

for i in range(100, 301):
    a = str(i)
    tmp = ''
    for j in a:
        if int(j) % 2 == 0:
            tmp += 'j'
        if len(tmp) == 3:
            list = list.append(tmp)
        tmp = ''



print(list)
    
print(','.join(list))
"""
