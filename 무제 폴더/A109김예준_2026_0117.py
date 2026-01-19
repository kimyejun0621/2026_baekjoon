from math import gcd
import sys
input = sys.stdin.readline

M = int(input())
num, den = 1, 1
direction = 0

for _ in range(M):
    a, b, s = map(int, input().split())
    num *= b
    den *= a
    if s == 1:
        direction ^= 1
    g = gcd(num, den)
    num //= g
    den //= g

print(direction, num // den)
