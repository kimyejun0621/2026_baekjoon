class Solution:
    def checkRecord(self, s: str) -> bool:
        # 조건 1: 'A'의 개수가 2개 미만인지 확인
        # 조건 2: "LLL" (3회 연속 지각)이 포함되어 있지 않은지 확인
        return s.count('A') < 2 and "LLL" not in s