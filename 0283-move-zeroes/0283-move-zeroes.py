class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        currIndex = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[currIndex], nums[i] = nums[i], nums[currIndex]
                currIndex += 1