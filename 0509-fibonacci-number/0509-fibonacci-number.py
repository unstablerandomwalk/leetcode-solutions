class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        a,b = 0,1
        for i in range(n-1):
            curr = a + b
            a,b = b,curr
        return b
