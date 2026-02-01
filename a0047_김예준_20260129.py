import sys

def solution():
    # 1. 단어 입력 받기
    word = sys.stdin.readline().strip()
    
    # 2. 10개씩 끊어서 출력하기
    # range(start, stop, step)을 사용하여 0부터 10씩 증가하며 반복
    for i in range(0, len(word), 10):
        # i부터 i+10까지 슬라이싱 (마지막 구간은 알아서 남은 만큼만 출력됨)
        print(word[i:i+10])

solution()