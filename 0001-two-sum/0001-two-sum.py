class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            req = target - nums[i]
            ind = nums.index(req) if req in nums else -1
            if ind != -1 and ind != i:
                return [i,ind]