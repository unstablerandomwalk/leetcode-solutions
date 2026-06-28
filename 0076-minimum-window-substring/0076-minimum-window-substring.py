from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        need = Counter(t)
        required = len(need)       
        have = 0                   
        window = {}
        start = 0
        minLength = float('inf')
        sub = ""
        for end in range(len(s)):
            c = s[end]
            window[c] = window.get(c, 0) + 1
            if c in need and window[c] == need[c]:
                have += 1
            while have == required:
                if end - start + 1 < minLength:
                    minLength = end - start + 1
                    sub = s[start:end + 1]
                left = s[start]
                window[left] -= 1
                if left in need and window[left] < need[left]:
                    have -= 1
                start += 1

        return sub