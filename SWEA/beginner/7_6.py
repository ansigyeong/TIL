#1
data = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
data_dic = {}
j = 0
for i in data:
    
    if i not in  data_dic:
        data_dic.setdefault(i, 1)
    
    
    j += 1
    data_dic.setdefault(i, j)

print(data_dic)

"""
#2
list = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
dic = {}

for i in list:
    if i not in dic:
        dic.setdefault(i, 1)
    else:
        dic[i] += 1
        
print(dic)
"""
