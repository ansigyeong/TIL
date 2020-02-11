def morelong(str1, str2):
    if len(str1) > len(str2):
        return str1
    if len(str1) < len(str2):
        return str2


s1, s2 = input().split(', ')
print(morelong(s1, s2))