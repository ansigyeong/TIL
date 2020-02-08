list = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
dic = {}

for i in list:
    if i not in dic:
        dic.setdefault(i, 1)
    else:
        dic[i] += 1
        
print(dic)