class Solution:
    def mySqrt(self, x: int) -> int:
        for i in range(x//2+1):
            if i*i <= x < (i+1)*(i+1):
                return i
                break
            elif x == (i+1) * (i+1):
                return i+1
                break
        