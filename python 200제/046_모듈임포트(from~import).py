# 학습 내용: 원하는 모듈만 임포트하여 간단하게 사용할 수 있는 방법에 대해 배웁니다.
# 힌트 내용: 계층 구조로 되어 있는 복잡한 모듈은 from ~ import로 임포트하면 편리하게 사용할 수 있습니다.

# from 모듈이름 import 함수이름
from time import sleep # time 모듈의 sleep() 함수만 임포트함

# from 패키지이름 import 모듈이름
from mypackage import mylib # mypackage의 mylib 모듈만 임포트함

#
from mypackage.mylib import reverse # mypackage.mylib 모듈의 reverse() 함수만 임포트함

sleep(1) # time 모듈의 sleep 함수 호출
print(mylib.add_txt('나는', ',파이썬이다')) # mypackage.mylib 모듈의 add_txt 함수를 호출함
print(reverse(1, 2, 3)) # mypackage.mylib 모듈의 reverse 함수를 호출함