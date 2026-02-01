def solution(s):
    answer = []
    # 단어의 시작인지 확인하는 플래그 (첫 문자는 항상 시작)
    is_first = True
    
    for char in s:
        if char == " ":
            answer.append(char)
            is_first = True  # 공백 다음 문자는 다시 첫 문자가 됨
        else:
            if is_first:
                answer.append(char.upper()) # 첫 글자는 대문자 (숫자면 변화 없음)
                is_first = False
            else:
                answer.append(char.lower()) # 나머지는 소문자
                
    return "".join(answer)