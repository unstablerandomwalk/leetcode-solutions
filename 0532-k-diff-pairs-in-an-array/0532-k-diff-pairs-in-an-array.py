class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        d = {}
        count = 0
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = 1
            else:
                d[nums[i]] += 1
        if k == 0:
            for i in d:
                if d[i] > 1:
                    count += 1
            return count
        for i in d:
            if i + k in d:
                count += 1
        return count
                
            