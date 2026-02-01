class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        
        # 1. 문자열 리스트를 사전순으로 정렬
        strs.sort()
        
        # 2. 가장 첫 단어와 가장 마지막 단어를 선택
        first = strs[0]
        last = strs[-1]
        
        ans = ""
        # 3. 두 단어를 앞에서부터 한 글자씩 비교
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                break
            ans += first[i]
            
        return ans