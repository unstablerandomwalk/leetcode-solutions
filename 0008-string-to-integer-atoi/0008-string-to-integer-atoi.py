class Solution:
    def myAtoi(self, s: str) -> int:
        digits = "0123456789"
        sign = 1
        num = 0
        s = s.strip()
        if not s:
            return 0
        i = 0
        if s[0] == '-':
            sign = -1
            i = 1
        elif s[0] == '+':
            i = 1
        while i < len(s) and s[i] in digits:
            num = num * 10 + int(s[i])
            i += 1
        result = sign * num
        return max(-2**31, min(result, 2**31 - 1))