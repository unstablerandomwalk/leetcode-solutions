class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currsum=0
        maxsum=float('-inf')
        for i in range(len(nums)):
            currsum+=nums[i]
            if currsum>maxsum:
                maxsum=currsum
            if currsum<0:
                currsum=0
        return maxsum