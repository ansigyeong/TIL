N = input()
dic = {}

for i in N:
    a = int(i)
    if a not in dic:
        dic.setdefault(a, 1)
    else:
        dic[a] += 1

# print(dic)


for i in range(10):
    if i == 9:
        print(i)
    else:
        print(i, end=' ')

for i in range(10):
    if i == 9:
        print(dic.get(i, 0))
    else:
        print(dic.get(i, 0), end=' ')

"""
#횟수를 저장하는 리스트 생성
array = [0]*10

num = int(input())

result = ""

#num이 0이 될때까지 반복하며 숫자체크
while num:
   array[num%10] += 1
   num //= 10

#0~9까지 출력하기
for i in range(0, 10):
   result += "%d " % i

print(result[0:len(result)-1])
#변수 초기화
result = ""
#나온횟수 출력하기
for i in range(0, 10):
   result += "%d " % array[i]
print(result[0:len(result)-1])
"""