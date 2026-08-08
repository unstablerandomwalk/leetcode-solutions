class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        greed = sorted(g, reverse=True)
        size = sorted(s, reverse = True)
        i,j = 0, 0
        count = 0
        while i < len(greed) and j < len(size):
            if greed[i] <= size[j]:
                count+=1
                i+=1
                j+=1
            else:
                i+=1
        return count