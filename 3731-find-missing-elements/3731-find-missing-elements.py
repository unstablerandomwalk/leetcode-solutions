class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        n = sorted(nums)
        l = []
        for i in range(1, len(n)):
            for j in range(n[i-1]+1, n[i]):
                l.append(j)
        return l
