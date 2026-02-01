from collections import deque

n = int(input())
q = deque(range(1, n + 1))

while len(q) > 1:
    q.popleft()       # 제일 위 카드 버림
    q.append(q.popleft())  # 다음 카드를 맨 아래로 이동

print(q[0])
