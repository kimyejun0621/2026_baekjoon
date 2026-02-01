import sys

def solution():
    n = int(sys.stdin.readline())
    group_word_count = 0
    
    for _ in range(n):
        word = sys.stdin.readline().strip()
        seen_chars = set()  # 이미 등장한 문자를 저장할 집합
        prev_char = ""      # 바로 이전 문자를 저장
        is_group_word = True
        
        for char in word:
            # 1. 처음 등장하는 문자인 경우
            if char not in seen_chars:
                seen_chars.add(char)
                prev_char = char
            # 2. 이미 등장했던 문자인 경우
            else:
                # 바로 이전 문자와 다르다면 그룹 단어가 아님!
                if char != prev_char:
                    is_group_word = False
                    break
                # 이전 문자와 같다면 연속해서 나오는 것이므로 통과
        
        if is_group_word:
            group_word_count += 1
            
    print(group_word_count)

solution()