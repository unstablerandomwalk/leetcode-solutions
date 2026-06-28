class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        d={}
        n=[]
        m = 0
        for x in points:
            d[m] = x[0]**2 + x[1]**2
            m=m+1
        s = sorted(d.items(), key = lambda x: x[1], reverse = False)
        for i in range(k):
            n.append(points[s[i][0]])
        return n        