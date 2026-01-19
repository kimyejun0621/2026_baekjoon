N, M = map(int, input().split())
packages = []
singles = []

for _ in range(M):
    p, s = map(int, input().split())
    packages.append(p)
    singles.append(s)

min_package = min(packages)
min_single = min(singles)

# 1. 패키지만으로 (N//6개 + 1개) 구매
option1 = ((N + 5) // 6) * min_package

# 2. 패키지 몇 개 + 나머지 낱개
option2 = (N // 6) * min_package + (N % 6) * min_single

# 3. 전부 낱개
option3 = N * min_single

print(min(option1, option2, option3))
