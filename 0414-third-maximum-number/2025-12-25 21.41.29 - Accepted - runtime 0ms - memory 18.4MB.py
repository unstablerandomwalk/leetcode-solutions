class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums_set=set(nums)
        nums_uni=list(nums_set)
        nums_uni.sort()
        if(len(nums_uni)>=3):
            return nums_uni[-3]
        else:
            return nums_uni[-1]
