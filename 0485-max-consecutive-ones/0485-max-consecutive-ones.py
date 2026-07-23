class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        total = 0
        curr = 0
        for i in nums:
            if i == 1:
                curr += 1
            else:
                total = max(total,curr)
                curr = 0
        return max(total,curr)