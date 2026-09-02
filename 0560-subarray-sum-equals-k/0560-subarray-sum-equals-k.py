class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        h = {0:1}
        curr_sum = 0
        count = 0
        for i in nums:
            curr_sum += i
            if(curr_sum - k) in h:
                count+=h[curr_sum-k]
            if curr_sum in h:
                h[curr_sum] +=1
            elif curr_sum not in h:
                h[curr_sum] = 1
        return count
            