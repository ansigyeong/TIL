# 학습 내용: 파이썬 모듈을 우리가 작성하는 코드로 임포트하는 방법을 이해합니다.
# 힌트 내용: 'import 모듈이름'으로 모듈이름에 해당하는 파이썬 모듈을 임포트합니다.

import time # 파이썬 내장 모듈인 time을 임포트함
import mylib # 내가 작성한 mylib 모듈을 임포트함
import mypackage.mylib # mypackage에 있는 mylib 모듈을 임포트함
# import aaa # (ModuleNotFoundError: No module named 'aaa', 존재하지 않는 모듈을 임포트 -> ImportError: No module named '모듈이름')

time.sleep(1) # time 모듈의 sleep 함수를 이용해 1초간 정지
print(mylib.add_txt('나는', '파이썬이다')) # mylib 모듈의 add_txt 함수를 호출함
print(mypackage.mylib.reverse(1, 2, 3)) # mypackage.mylib 모듈의 reverse 함수를 호출함

# mypackage만 임포트하고, mypackage.mylib.add_txt()를 호출 -> AttributeError: module 'mypackage' has no attribute 'mylib'

