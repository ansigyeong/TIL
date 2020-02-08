list = ["가위", "바위", "보"]

# def Check(a, b):
#     if (a == b):
#         print("비겼습니다!")
#     elif (a == lis[0] and b == lis[1]) or (b == lis[0] and a == lis[1]):
#         print("바위가 이겼습니다!")
#     elif (a == lis[0] and b == lis[2]) or (b == lis[0] and a == lis[2]):
#         print("가위가 이겼습니다!")
#     elif (a == lis[1] and b == lis[2]) or (b == lis[1] and a == lis[2]):
#         print("보가 이겼습니다!")
#
# name1, name2 = input(), input()
# t1, t2 = input(), input()
# Check(t1, t2)

def game(a, b):
    if a == b:
        print("무승부입니다.")
    elif (a == list[0] and b == list[2]) or (a == list[2] and b == list[0]):
        print('가위가 이겼습니다!')
    elif (a == list[1] and b == list[0]) or (a == list[0] and b == list[1]):
        print('바위가 이겼습니다!')
    else:
        print('보가 이겼습니다!')

name1, name2 = input(), input()
g, m = input(), input()

game(g, m)

# def game(a, b):
#
#     if a == 가위:
#         if b == 바위:
#             return False
#         elif b == 보:
#             return True
#         else:
#             return Draw
#     if a == 바위:
#         if b == 보:
#             return False
#         elif b == 가위:
#             return True
#         else:
#             return Draw
#     if a == 보:
#         if b == 가위:
#             return False
#         elif b == 바위:
#             return True
#         else:
#             return Draw
#
# user1 = input()
# user2 = input()
#
# result1 = input()
# result2 = input()
#
# if game(result1, result2):
#     print('{}가 이겼습니다!'.format(a))
#
# if game(result1, result2) == False:
#     print('{}가 이겼습니다!'.format(b))
#
# if game(result1, result2) == Draw:
#     print('무승부입니다.')