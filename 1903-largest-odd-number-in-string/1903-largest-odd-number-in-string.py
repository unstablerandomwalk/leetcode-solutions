class Solution:
    def largestOddNumber(self, num: str) -> str:
        n = num[::-1]
        index = len(num)
        for i in range(len(n)):
            if int(n[i]) % 2 == 1:
                index = i
                break
        a = n[index:]
        return a[::-1]