class Solution:
    def longestPalindrome(self, s: str) -> str:
        sub = ""
        def expand(start, end):
            while start >= 0 and end < len(s) and s[start] == s[end]:
                start -= 1
                end += 1
            return s[start+1: end]
        for i in range(len(s)):
            odd = expand(i,i)
            even = expand(i,i+1)
            sub = max(sub,odd,even, key = len)
        return sub