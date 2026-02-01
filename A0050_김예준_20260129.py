import sys

def solve():
    # 1. 암호화된 단어 입력 받기
    word = sys.stdin.readline().strip()
    result = []
    
    for char in word:
        # 문자의 아스키 코드 값에서 3을 뺌
        # A(65), B(66), C(67) 처럼 범위를 벗어나는 경우 처리
        # 'D' -> 'A' (68-3 = 65)
        # 'A' -> 'X' (65-3 = 62 -> 여기서 26을 더해주면 88, 즉 'X')
        
        original_code = ord(char) - 3
        
        # 'A'의 아스키 코드 값인 65보다 작아지면 알파벳 끝(X, Y, Z)으로 순환
        if original_code < ord('A'):
            original_code += 26
            
        result.append(chr(original_code))
    
    # 리스트를 문자열로 합쳐서 출력
    print("".join(result))

solve()