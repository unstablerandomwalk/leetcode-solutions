class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count0 = nums.count(0)
        count1 = nums.count(1)
        count2 = nums.count(2)
        index = 0
        while index < len(nums):
            if index < count0:
                nums[index] = 0
            elif index < count0+count1:
                nums[index] = 1
            else:
                nums[index] = 2
            index += 1