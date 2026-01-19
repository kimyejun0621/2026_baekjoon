T = int(input())
for _ in range(T):
    S = input()
    appeared = set(S)
    total = 0
    for c in range(ord('A'), ord('Z') + 1):
        if chr(c) not in appeared:
            total += c
    print(total)
