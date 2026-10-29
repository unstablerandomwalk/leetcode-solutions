class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        count = 0
        last = len(nums) - 1
        first = len(nums)
        for i in range(len(nums)):
            while (nums[i] + nums[last]) > upper and last >= i:
                last-=1
            while (nums[i] + nums[first-1]) >= lower and first > 0:
                first -=1
            left = max(first, i+1)
            if last >= left:
                count += last-left+1
        return count

    