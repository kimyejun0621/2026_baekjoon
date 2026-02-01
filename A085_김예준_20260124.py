def digit_sum(s):
    return sum(int(ch) for ch in s if ch.isdigit())

n = int(input())
serials = [input().strip() for _ in range(n)]

serials.sort(key=lambda x: (len(x), digit_sum(x), x))

for s in serials:
    print(s)
