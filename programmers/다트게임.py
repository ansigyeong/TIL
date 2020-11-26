# 문자열 처리

# str.isnumeric() => '½' 같은 특수 문자도 숫자로 판별함
# str.isdigit() => '숫자처럼 생긴' 모든 글자를 숫자로 판별함
# str.isdecimal() => '0 ~ 9' 10진수만 숫자로 판별함

def solution(dartResult):
    nums = [0]
    
    for s in dartResult:
        if s == 'S':
            nums[-1] **= 1
            nums.append(0)
        elif s == 'D':
            nums[-1] **= 2
            nums.append(0)
        elif s == 'T':
            nums[-1] **= 3
            nums.append(0)
        elif s == '*':
            nums[-2] *= 2
            if len(nums) > 2:
                nums[-3] *= 2
        elif s == '#':
            nums[-2] *= -1
            nums.append(0)
        else:
            # 자릿수 올림
            nums[-1] *= 10
            nums[-1] += int(s)
            
    return sum(nums)

# def solution(dartResult):
#     # * => 해당, 바로 앞 * 2, # => 해당 -1
#     answer = 0
#     temp = []
#     len_dartResult = len(dartResult)
#     flag = False
#     for i in range(len_dartResult):
#         if dartResult[i].isdecimal() and flag == False:
#             temp.append(int(dartResult[i]))
#             flag = True
#         elif dartResult[i].isdecimal() and flag == True:
#             temp.pop()
#             temp.append(10)
#             flag = False
#         elif dartResult[i] == 'S':
#             n = temp.pop()
#             n **= 1
#             temp.append(n)
#             flag = False
#         elif dartResult[i] == 'D':
#             n = temp.pop()
#             n **= 2
#             temp.append(n)
#             flag = False
#         elif dartResult[i] == 'T':
#             n = temp.pop()
#             n **= 3
#             temp.append(n)
#             flag = False
#         elif dartResult[i] == '*':
#             length = len(temp)
#             if length >= 2:
#                 n = temp.pop()
#                 m = temp.pop()
#                 n *= 2
#                 m *= 2
#                 temp.append(m)
#                 temp.append(n)
#             else:
#                 n = temp.pop()
#                 n *= 2
#                 temp.append(n)
#         elif dartResult[i] == '#':
#             n = temp.pop()
#             n *= -1
#             temp.append(n)
#     answer = sum(temp)
#     return answer