def is_palindrome(n):
    return str(n) == str(n)[::-1]

T = int(input())
for _ in range(T):
    N = input()
    reversed_N = N[::-1]
    total = int(N) + int(reversed_N)
    if is_palindrome(total):
        print("YES")
    else:
        print("NO")
