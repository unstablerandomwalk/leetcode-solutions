class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l = [0] * len(temperatures)
        stack=[]
        for i in range(len(temperatures)):
            while stack and (temperatures[i] > temperatures[stack[-1]]):
                x = stack.pop()
                l[x] = i - x
            stack.append(i)
        return l
