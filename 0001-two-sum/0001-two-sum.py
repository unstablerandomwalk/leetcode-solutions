class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            n = target - nums[i]
            if n in d:
                return [i,d[n]]
            d[nums[i]]=i
        return[]