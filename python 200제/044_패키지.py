# 학습 내용: 파이썬 모듈의 계층적인 구조인 파이썬 패키지에 대해 이해합니다.
# 힌트 내용: 파이썬 모듈이 하나의 파이썬 파일이라면 패키지는 디렉터리로 보면 됩니다.

import mypackage.mylib

ret1 = mypackage.mylib.add_txt('대한민국', '1등')
ret2 = mypackage.mylib.reverse(1, 2, 3)

print(ret1)
print(ret2)