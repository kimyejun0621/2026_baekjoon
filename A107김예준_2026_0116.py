A, B = map(int, input().split())

sequence = []
i = 1
while len(sequence) < B:
    sequence.extend([i] * i)
    i += 1

print(sum(sequence[A-1:B]))
