class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        elif len(nums) == 2:
            return 0 if nums[0] > nums[1] else 1
        l = [float('-inf')]
        l.extend(nums)
        l.append(float('-inf'))
        for i in range(len(l)-2):
            if l[i+1] > l[i] and l[i+1] > l[i+2]:
                return i
                break