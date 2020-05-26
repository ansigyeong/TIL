vlqhskcl = []

for i in range(1, 11):
    if i == 1 or i == 2:
        n = 1
        vlqhskcl.append(n)
    if i > 2:
        n = vlqhskcl[i-3] + vlqhskcl[i-2]
        vlqhskcl.append(n)

print(vlqhskcl)