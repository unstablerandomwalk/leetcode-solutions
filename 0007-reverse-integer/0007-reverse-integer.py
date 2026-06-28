class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        s = str(abs(x))
        y = s[::-1]
        result = int(y) * sign
        if result < -2**31 or result > 2**31 - 1:
            return 0
        return result