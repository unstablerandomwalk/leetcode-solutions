class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i in d:
                d[i] = 2
            else:
                d[i] = 1
        for a,b in d.items():
            if b == 1:
                return a