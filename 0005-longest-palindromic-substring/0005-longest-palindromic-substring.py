class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        t = "#" + "#".join(s) + "#"
        sub = ""
        for i in range(len(t)):
            start, end = i, i
            while start >= 0 and end < len(t) and t[start] == t[end]:
                if end - start + 1 > len(sub):
                    sub = t[start:end + 1]
                start -= 1
                end += 1
        return sub.replace("#", "")