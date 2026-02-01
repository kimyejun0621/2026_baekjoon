import sys

def is_vowel(char):
    return char in "aeiou"

def solve():
    while True:
        s = sys.stdin.readline().strip()
        if s == "end":
            break
            
        has_vowel = False
        is_acceptable = True
        vowel_consecutive = 0 # 연속된 모음 개수
        consonant_consecutive = 0 # 연속된 자음 개수
        
        for i in range(len(s)):
            char = s[i]
            
            # 조건 1: 모음 포함 여부 확인
            if is_vowel(char):
                has_vowel = True
                vowel_consecutive += 1
                consonant_consecutive = 0
            else:
                consonant_consecutive += 1
                vowel_consecutive = 0
            
            # 조건 2: 모음/자음 3개 연속 확인
            if vowel_consecutive >= 3 or consonant_consecutive >= 3:
                is_acceptable = False
                break
                
            # 조건 3: 같은 글자 연속 2번 확인 (ee, oo 제외)
            if i > 0 and s[i] == s[i-1]:
                if s[i] not in "eo":
                    is_acceptable = False
                    break
        
        # 모든 검사 후 최종 판단
        if not has_vowel:
            is_acceptable = False
            
        if is_acceptable:
            print(f"<{s}> is acceptable.")
        else:
            print(f"<{s}> is not acceptable.")

solve()