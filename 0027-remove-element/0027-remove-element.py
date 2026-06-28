class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums.sort()
        while val in nums:
            nums.remove(val)
        k = len(nums)
        return k 