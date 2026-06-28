class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n=len(nums)
        previous=0
        d={0:-1}
        for i in range(n):
            previous = (previous + nums[i])%k
            if previous in d:
                if i - d[previous]>=2:
                    return True
            else:
                d[previous]=i
        return False