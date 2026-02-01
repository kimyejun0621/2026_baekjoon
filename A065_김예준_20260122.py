import sys

N = int(sys.stdin.readline())
points = []

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    points.append((x, y))

# x 기준 오름차순, x가 같으면 y 기준 오름차순 정렬
points.sort()

for x, y in points:
    print(x, y)
