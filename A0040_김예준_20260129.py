class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        # 1. 모음 집합 정의 (O(1) 조회를 위해 set 사용)
        vowels = set("aeiouAEIOU")
        
        # 2. 문자열의 중간 지점 계산
        mid = len(s) // 2
        
        # 3. 앞부분(a)과 뒷부분(b) 나누기
        a = s[:mid]
        b = s[mid:]
        
        # 4. 각 부분의 모음 개수 세기
        count_a = sum(1 for char in a if char in vowels)
        count_b = sum(1 for char in b if char in vowels)
        
        # 5. 개수가 같은지 비교
        return count_a == count_b