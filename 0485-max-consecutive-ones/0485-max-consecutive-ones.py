class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        total = 0
        curr = 0
        for i in nums:
            if i == 1:
                curr += 1
                total = max(total,curr)
            else:
                curr = 0
        return total