# 학습 내용: 파이썬 모듈을 이해하고 자신의 코드에 모듈을 포함시키는 방법을 배웁니다.
# 힌트 내용: 파이썬 모듈은 보통 하나의 독립된 파이썬 소스 파일로 구성되어 있습니다.

import time # 파이썬 내장 모듈인 time 모듈을 임포트(import)함

print('5초간 프로그램을 정지합니다.')
time.sleep(5) # time 모듈이 제공하는 sleep()을 호출함
print('5초가 지났습니다.')

import mylib # mylib 모듈을 임포트(import)함

ret1 = mylib.add_txt('대한민국', '1등') # mylib 모듈이 제공하는 add_txt()를 호출함
ret2 = mylib.reverse(1, 2, 3) # mylib 모듈이 제공하는 reverse()

print(ret1)
print(ret2)