class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # 1. nums2의 각 원소에 대한 'Next Greater Element'를 저장할 딕셔너리
        mapping = {}
        # 2. 큰 숫자가 나타나길 기다리는 숫자들을 담는 스택
        stack = []
        
        for num in nums2:
            # 현재 숫자(num)가 스택 맨 위의 숫자보다 크다면?
            # 스택에 있던 숫자의 'Next Greater'는 바로 현재 숫자가 됩니다.
            while stack and stack[-1] < num:
                waiting_num = stack.pop()
                mapping[waiting_num] = num
            
            # 현재 숫자도 다음 큰 숫자를 찾기 위해 스택에 넣습니다.
            stack.append(num)
            
        # 3. 스택에 남아있는 숫자들은 오른쪽에 더 큰 숫자가 없는 경우입니다.
        # (문제 요구사항에 따라 딕셔너리에 없는 값은 -1로 처리합니다)
        
        # 4. nums1의 순서에 맞춰 결과를 생성합니다.
        return [mapping.get(n, -1) for n in nums1]