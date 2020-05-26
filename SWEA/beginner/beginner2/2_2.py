# 4차시

python = 'Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'
vowels = ['a', 'e', 'i', 'o', 'u']
new_python = ''

for i in python:
    if i not in vowels:
        new_python += i

print(new_python)