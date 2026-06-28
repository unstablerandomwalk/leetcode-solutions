class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        li, ro = 0, len(height) - 1
        left_max, right_max = 0,0
        ans = 0
        while li < ro:
            if height[li] < height[ro]:
                if left_max <= height[li]:
                    left_max = height[li]
                else:
                    ans += (left_max - height[li])
                li += 1
            else:
                if right_max <= height[ro]:
                    right_max = height[ro]
                else:
                    ans += (right_max - height[ro])
                ro -=1
        
        return ans