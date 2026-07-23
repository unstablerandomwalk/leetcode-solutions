class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        nums.sort()
        l = 0
        cur = 0
        for r in range(len(nums)):
            cur += nums[r]
            if (r - l + 1) * nums[r] - cur > k:
                cur -= nums[l]
                l += 1
        return len(nums) - l