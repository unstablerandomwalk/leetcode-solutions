import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap=[-x for x in stones]
        heapq.heapify(max_heap)
        while (len(max_heap)>1):
            x1=heapq.heappop(max_heap)
            x2=heapq.heappop(max_heap)
            x = -((-x1) - (-x2))
            if x != 0:
                heapq.heappush(max_heap, x)
        if(len(max_heap)==1):
            return -heapq.heappop(max_heap)
        else:
            return 0
