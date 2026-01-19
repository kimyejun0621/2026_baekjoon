N = int(input())

def is_hansu(n):
    digits = list(map(int, str(n)))
    if len(digits) <= 2:
        return True
    diff = digits[1] - digits[0]
    for i in range(2, len(digits)):
        if digits[i] - digits[i - 1] != diff:
            return False
    return True

count = 0
for i in range(1, N + 1):
    if is_hansu(i):
        count += 1

print(count)
