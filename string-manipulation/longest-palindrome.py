class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1] or len(s) < 2:
            return s
        result = ''
        
        def expand(left: int, right: int) -> str:
            while left >= 0 and right <= len(s) and s[left] == s[right - 1]:
                left -= 1
                right += 1
            return s[left + 1:right - 1]
        
        for i in range(len(s) - 1):
            result = max(result, expand(i, i+1), expand(i, i+2), key = len)
        return result
        
