class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = []
        opened = 0
        
        for char in s:
            if char == '(':
                # 이미 열린 괄호가 1개 이상 있다면, 
                # 현재 '('는 '가장 바깥쪽'이 아니므로 결과에 포함합니다.
                if opened > 0:
                    res.append(char)
                opened += 1
            else: # char == ')'
                opened -= 1
                # 닫고 난 뒤에도 열린 괄호가 0보다 크다면, 
                # 현재 ')'는 '가장 바깥쪽'이 아니었으므로 결과에 포함합니다.
                if opened > 0:
                    res.append(char)
                    
        return "".join(res)