class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        if len(nums) < 4:
            return max(nums)
        nums2 = nums.copy()
        nums.pop()
        nums2.pop(0)
        money1 = [0,nums[0]]
        money2 = [0,nums2[0]]
        for i in range(2,len(nums)+1):
            money1.append(max(money1[i-2] + nums[i-1], money1[i-1]))
        for i in range(2,len(nums2)+1):
            money2.append(max(money2[i-2] + nums2[i-1], money2[i-1])) 
        return max(money1[-1], money2[-1])       