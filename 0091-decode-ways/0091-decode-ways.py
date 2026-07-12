class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0
        r,t = 1,1
        for i in range(2, len(s)+1):
            cur = 0
            if s[i-1] != "0":
                cur += t
            if 10<= int(s[i-2: i]) <= 26:
                cur += r
            r,t = t,cur
        return t