class Solution:
    def nextGreaterElement(self, nums1, nums2):
        r = []
        for i in nums1:
            j = nums2.index(i) + 1
            found = False
            while j < len(nums2):
                if nums2[j] > i:
                    r.append(nums2[j])
                    found = True
                    break
                j += 1
            if not found:
                r.append(-1)
        return r