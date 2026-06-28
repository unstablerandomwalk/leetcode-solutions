class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        nums.append(target)
        nums.sort()
        for x in range(len(nums)):
            if nums[x] == target:
                return x
                break 