class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        filtered = [c.lower() for c in s if c.isalnum()]
        return filtered == filtered[::-1]
