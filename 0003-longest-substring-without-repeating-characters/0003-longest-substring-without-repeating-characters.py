class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        if not s:
            return 0
        left = 0
        right = 0
        length = 0
        while right < len(s):
            if s[right] in seen:
                left = max(left, seen[s[right]]+1)
            seen[s[right]] = right
            l = right-left+1
            length = max(length, l)
            right+=1
        return length
            
            
                
