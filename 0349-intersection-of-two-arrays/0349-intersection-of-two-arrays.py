class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        for i in nums1:
            if i not in d:
                d[i] = 1
        for i in nums2:
            if i in d and d[i] == 1:
                d[i] = 2

        l = []
        for i in d:
            if d[i] == 2:
                l.append(i)
        return l