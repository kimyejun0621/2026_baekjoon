class Solution:
    def calPoints(self, operations: list[str]) -> int:
        stack = []
        
        for op in operations:
            if op == '+':
                # 마지막 두 점수의 합을 추가
                stack.append(stack[-1] + stack[-2])
            elif op == 'D':
                # 마지막 점수의 2배를 추가
                stack.append(stack[-1] * 2)
            elif op == 'C':
                # 마지막 점수를 제거
                stack.pop()
            else:
                # 숫자인 경우 정수로 변환하여 추가
                stack.append(int(op))
        
        # 스택에 남은 모든 점수의 합을 반환
        return sum(stack)