# stack 기본

- 선형구조 (-> 자료간의 관계가 1대1의 관계를 가짐)

  *참고: 비선형구조 -> 자료간의 관계가 1대N의 관계를 가짐 e.g.) 트리

- 후입선출(LIFO, Last-In-First-Out)



### 자료구조

***자료를 선형으로 저장할 저장소가 필요함 => List***

- 저장소 자체를 stack이라 부르기도 함
- 스택에서 마지막에 삽입된 원소의 위치: top



### 연산

1. 삽입: push
2. 삭제: pop
3. isEmpty: 스택이 공백인지 아닌지 확인하는 연산
4. peek: top에 있는 item을 반환하는 연산



### 슈도코드

```python
def push(item):
  s.append(item)
def pop():
  if len(s) == 0:
    print("Stack is Empty!")
    return
  else:
    return s.pop(-1)
  
s = []

push(1)
push(2)
push(3)

print("pop item =>", pop())
print("pop item =>", pop())
print("pop item =>", pop())
```



### 스택 구현 고려사항

- 장점: 구현이 용이하다는 장점

- 단점: 리스트의 크기를 변경하는 작업은 내부적으로 큰 overhead 발생 작업으로 많은 시간이 소요

해결방법

1. 리스트의 크기가 변동되지 않도록 배열처럼 크기를 미리 정해놓고 사용하는 방법
2. 동적 연결리스트를 이용하여 저장소를 동적으로 할당하여 스택을 구현하는 방법