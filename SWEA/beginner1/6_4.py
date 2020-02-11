# import sys
# sys.stdin = open("6_4.txt", "r")

game = ["가위", "바위", "보"]

Man1 = input()
Man2 = input()

# print(Man1)
# print(Man2)

if Man1 == Man2:
    result = 'Draw'
    
for i in range(len(game)):
    for j in range(i+1, len(game) + 1):
        if Man1 == i and Man2 == j:
            print('Result : Man2 Win!')
            
print('Result : Man1 Win!')