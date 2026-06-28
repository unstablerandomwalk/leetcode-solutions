class Solution:
    def climbStairs(self, n: int) -> int:
        a = 1
        b = 1
        for x in range(n-1):
            a,b = a+b,a
        return(a)

        