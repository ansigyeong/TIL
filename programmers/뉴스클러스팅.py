# 자카드 유사도
# J(A, B) => 두 집합의 교집합 크기를 두 집합의 합집합 크기로 나눈 값
# 집합 A와 집합 B가 모두 공집합일 때 => J(A, B) = 1

# 다중집합 A = {"1", "1", "1"}, B = {"1", "1", "1", "1", "1"}
# 교집합 => min(3, 5) 합집합 => max(3, 5)

import re
import collections


def solution(str1, str2):
    # 두 글자씩 끊어서 다중집합 구성
    str1s = [
        str1[i:i+2].lower()
        for i in range(len(str1) - 1)
        if re.findall('[a-z]{2}', str1[i:i+2].lower()) # 두 글자씩 다중집합 만들기(공백, 숫자, 특수문자 버리기)
    ]
    str2s = [
        str2[i:i+2].lower()
        for i in range(len(str2) - 1)
        if re.findall('[a-z]{2}', str2[i:i+2].lower())
    ]
    
    # 교집합 계산
    intersection = sum((collections.Counter(str1s) & collections.Counter(str2s)).values()) # couter => dict key 몇 개인지 value로 나타냄 / values => dict value
    
    # 합집합 계산
    union = sum((collections.Counter(str1s) | collections.Counter(str2s)).values())
    
    # 자카드 유사도 계산
    jaccard_sim = 1 if union == 0 else intersection / union
    return int(jaccard_sim * 65536)




# def solution(str1, str2):
#     # 대소문자 무시 => .lower()
#     str1 = str1.lower()
#     str2 = str2.lower()
    
    
#     # 두 글자씩 다중집합 만들기(공백, 숫자, 특수문자 버리기)
#     str1_set = []
#     str2_set = []
    
#     for n in range(0, len(str1) - 1):
#         if str1[n].isalpha() and str1[n+1].isalpha(): # isalpha isalpha isalpha
#             str1_set.append(str1[n] + str1[n+1])
    
#     for n in range(0, len(str2) - 1):
#         if str2[n].isalpha() and str2[n+1].isalpha():
#             str2_set.append(str2[n] + str2[n+1])
    
#     len_str1_set = len(str1_set)

#     intersection = 0 # 교집합
#     union = 0 # 합집합
    
#     for _ in range(len_str1_set):
#         temp = str1_set.pop()
#         if temp in str2_set:
#             intersection += 1
#             union += 1
#             str2_set.remove(temp)
#         else:
#             union += 1
    
#     union += len(str2_set)
    
#     if len(str1_set) == 0 and len(str2_set) == 0:
#         answer = int(1 * 65536)
#     else:
#         answer = int((intersection / union) * 65536)
    
#     return answer