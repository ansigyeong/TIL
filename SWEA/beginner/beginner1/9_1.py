import datetime
name = input()
time = 100 - int(input())
year = datetime.datetime.now().year - 1 + time

print('%s(은)는 %d년에 100세가 될 것입니다.' %(name, year))

# name = input()
# age = int(input())
#
# def hundred(n, g):
#     how_plus = 100 - g
#     result = 2019 + how_plus
#     print('{}(은)는 {}년에 100세가 될 것입니다.'.format(n, result))
#
# hundred(name, age)

