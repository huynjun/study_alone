### python: stack 쌓기





##### 삽입(5)-삽입(2)-삽입(3)-삽입(7)-삭제()-삽입(1)-삽입(4)-삭제()

```python
stack=[]

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()  #제거
stack.append(1)
stack.append(4)
stack.pop()

print(stack[::-1]) # 최상단 원소부터 출력
print(stack) #최하단 원소부터 출력
```





## 큐 자료구조

- 먼저 들어 온 데이터가 먼저 나가는 형식(선입선출)의 자료구조 입니다.
- 큐는 입구와 출구가 모두 뚫려 있는 터널과 같은 형태로 시각화 할 수 있습니다.

#### python 큐자료

```python
from collections import deque
#큐(Qeue) 구현을 위에 deque 라이브러리 사용
queue=deque()

#삽입(5)-삽입(2)-삽입(3)-삽입(7)-삭제()-삽입(1)-삽입(4)-삭제()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) # 먼저 들어온 순서대로 출력
queue.reverse() #역순으로 바꾸기
print(queue) # 나중에 들어온 원소부터 출력

```







