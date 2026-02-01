import sys

input = sys.stdin.readline
n = int(input())
members = []

for i in range(n):
    age, name = input().split()
    members.append((int(age), i, name))  # 가입 순서인 i를 함께 저장

members.sort(key=lambda x: (x[0], x[1]))  # 나이순, 가입순 정렬

for age, _, name in members:
    print(f"{age} {name}")
