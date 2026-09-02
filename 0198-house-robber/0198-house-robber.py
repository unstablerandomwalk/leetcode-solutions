class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        money = [0, nums[0]]
        for i in range(2, len(nums)+1):
            money.append(max(money[i-2] + nums[i-1], money[i-1]))
        return money[-1]