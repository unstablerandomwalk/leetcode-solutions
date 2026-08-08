class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            p = 1
            copy = n
            while copy > 0:
                p *= (copy%10)
                copy = copy//10
            if p % t != 0:
                n+=1
            else:
                return n