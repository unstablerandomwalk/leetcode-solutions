class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        n = []
        for x in nums:
            d[x] = d.get(x,0) + 1
        print(d)
        sorted_items = sorted(d.items(), key=lambda x: x[1], reverse=True)
        for i in range(k):
            n.append(sorted_items[i][0])
        return n
