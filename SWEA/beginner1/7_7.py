score = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]

#list = []

#3.
result = 0
while score:
    k = score.pop()
    if k >= 80:
        result += k
print(result)


#2.

# while score:
#     for i in score:
#         if i >= 80:
#             a = score.pop(index(i))
#             list.append(a)

# print(list)

#1.

# while score:
#     if score.pop() >= 80:
#         a = score.pop()
#         list.append(a)
#     else:
#         score.pop()

# print(list)        

#print(sum(list))        