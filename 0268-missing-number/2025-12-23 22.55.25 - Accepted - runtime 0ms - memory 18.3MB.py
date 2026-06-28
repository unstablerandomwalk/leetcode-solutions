class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        nums_sum=int((n*(n+1))/2)
        actual_sum=sum(nums)
        return nums_sum-actual_sum
