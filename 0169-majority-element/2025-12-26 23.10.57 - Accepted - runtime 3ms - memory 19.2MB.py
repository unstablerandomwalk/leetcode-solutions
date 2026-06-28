class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=set(nums)
        for i in n:
            if nums.count(i) >= (len(nums)//2)+1:
                return i