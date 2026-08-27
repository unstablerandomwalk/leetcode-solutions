class Solution:
    def maxDepth(self, s: str) -> int:
        h = []
        count = 0
        for i in s:
            if i == '(':
                h.append(i)
            elif i == ')':
                h.pop()
            count = max(count, len(h))
        return count