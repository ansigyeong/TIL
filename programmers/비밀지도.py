# 비트 연산자 OR 이용

# 진수 변환 내장 함수 
# 1. bin() -> 숫자(10진수)를 2진수 형태의 문자열로 변환
# 2. oct() -> 숫자(10진수)를 8진수 형태의 문자열로 변환
# 3. hex() -> 숫자(10진수)를 16진수 형태의 문자열로 변환

def solution(n, arr1, arr2):
    maps = []
    for i in range(n):
      maps.append(
        bin(arr1[i] | arr2[i])[2:] # 앞에 두 자리 이상한 거(0b, 0o, 0x) 있음
        .zfill(n) # 문자열 앞 0으로 채우기, 전체 자리수 n
        .replace('1', '#')
        .replace('0', ' ')
      )
    return maps  