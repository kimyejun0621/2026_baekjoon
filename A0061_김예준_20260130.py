class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        
        while columnNumber > 0:
            # 1. 1부터 시작하는 체계를 0부터 시작하도록 보정
            columnNumber -= 1
            
            # 2. 26으로 나눈 나머지를 구함 (0=A, 1=B, ..., 25=Z)
            remainder = columnNumber % 26
            
            # 3. 아스키 코드를 이용해 문자로 변환하여 리스트에 추가
            # ord('A')는 65이므로, 0이면 'A', 1이면 'B'가 됨
            res.append(chr(ord('A') + remainder))
            
            # 4. 다음 자리수를 위해 26으로 나눈 몫으로 갱신
            columnNumber //= 26
            
        # 5. 뒤에서부터 구했으므로 뒤집어서 합침
        return "".join(reversed(res))