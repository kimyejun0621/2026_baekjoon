import sys

def solve():
    # 1. 다이얼에 적힌 알파벳 묶음을 리스트로 정의
    # 각 인덱스 + 2가 해당 숫자가 됩니다.
    # 예: dial[0]은 숫자 2에 해당하며 'ABC'가 있음
    dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
    
    # 2. 단어 입력 받기
    word = sys.stdin.readline().strip()
    
    total_time = 0
    
    # 3. 단어의 각 알파벳 확인
    for char in word:
        for i in range(len(dial)):
            # 알파벳이 위치한 묶음을 찾으면
            if char in dial[i]:
                # 걸리는 시간 = 숫자(i + 2) + 1초
                # 즉, 인덱스 i에 3을 더하면 됩니다.
                total_time += (i + 3)
                break
                
    print(total_time)

solve()