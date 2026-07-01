class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for x in range(len(nums)):
            if nums[x] == nums[x+1]:
                return nums[x]