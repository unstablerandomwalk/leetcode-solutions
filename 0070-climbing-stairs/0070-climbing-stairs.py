class Solution:
    def climbStairs(self, n: int) -> int:
        temp = [0,1]
        for i in range(n):
            temp.append(temp[i]+temp[i+1])
        return temp[-1]