class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        def canFinish(k, piles, h):
            time = 0
            for i in piles:
                time += (i + k - 1) // k
            if time > h:
                return False
            return True
        while left < right:
            mid = (left + right) // 2
            if canFinish(mid, piles, h):
                right = mid
            else:
                left = mid+1
        return left
            