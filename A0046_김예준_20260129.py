import sys

def solution():
    # 1. 입력 받기
    # n이 첫 줄에 주어지고, 그 다음 n개의 줄에 성이 주어집니다.
    n = int(sys.stdin.readline())
    
    # 각 알파벳 첫 글자의 빈도를 저장할 딕셔너리
    counts = {}
    
    for _ in range(n):
        last_name = sys.stdin.readline().strip()
        first_char = last_name[0] # 성의 첫 글자 추출
        
        # 딕셔너리에 개수 기록
        counts[first_char] = counts.get(first_char, 0) + 1
    
    # 2. 5명 이상인 성의 첫 글자 찾기
    result = []
    for char, count in counts.items():
        if count >= 5:
            result.append(char)
    
    # 3. 결과 출력
    if not result:
        print("PREDAJA")
    else:
        # 사전순으로 정렬하여 공백 없이 출력
        print("".join(sorted(result)))

solution()