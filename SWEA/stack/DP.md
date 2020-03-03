# DP

- DP(Dynamic Programming, 동적 계획법)

  > - 그리디 알고리즘과 같이 **최적화** 문제를 해결하는 알고리즘
  > - 먼저 입력 크기가 작은 부분 문제들을 모두 해결한 후에 그 해들을 이용하여 보다 큰 크기의 부분 문제들을 해결함
  > - 최종적으로 원래 주어진 입력의 문제를 해결함

  > e.g) 피보나치 수를 구하는 함수에 DP 적용하기
  >
  > *피보나치 수는 부분 문제의 답으로부터 본 문제의 답을 얻을 수 있는 최적 부분 구조로 이루어져 있어 DP를 적용할 수 있음*
  >
  > 1. 문제를 부분 문제로 분할함
  >
  >    - Fibonacci(n) 함수는 Fibonacci(n-1)과 Fibonacci(n-2)의 합
  >    - Fibonacci(n-1)은 Fibonacci(n-2)와 Fibonacci(n-3)의 합
  >    - Fibonacci(2)는 Fibonacci(1)과 Fibonacci(0)의 합
  >    - Fibonacci(n)은 Fibonacci(n-1), Fibonacci(n-2), ⋯, Fibonacci(2) Fibonacci(1), Fibonacci(0)의 부분집합으로 나뉨
  >
  > 2. 부분 문제로 나누는 일을 끝냈으면 가장 작은 부분 문제부터 해를 구함
  >
  > 3. 그 결과는 테이블에 저장하고, 테이블에 저장된 부분 문제의 해를 이용하여 상위 문제의 해를 구함
  >
  >    |  테이블 인덱스   | [0]  | [1]  | [2]  | [3]  | [4]  |  ⋯   |   [n]   |
  >    | :--------------: | :--: | :--: | :--: | :--: | :--: | :--: | :-----: |
  >    | 저장되어 있는 값 |  0   |  1   |  1   |  2   |  3   |  ⋯   | fibo(n) |
  >
  > ```python
  > # 피보나치 수를 DP에 적용한 알고리즘
  > 
  > def fibo2(n):
  >   f = [0, 1]
  >   
  >   # 반복문을 이용하여 작은 값부터 상위로 구해나감
  >   for i in range(2, n+1):
  >     f.append(f[i-1] + f[i-2])
  >     
  >   return f[n]
  > ```

  

- DP의 구현 방식

  1. recursive 방식: fibo1() 

     재귀적 구조는 내부에 시스템 호출 스택을 사용하는 **overhead**가 발생할 수 있음

  2. iterative 방식: fibo2()

     Memoization을 재귀적 구조에 사용하는 것보다 반복적 구조로 DP를 구현한 것이 **성능 면에서 보다 효율적임**

     
