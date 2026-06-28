class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = {}
        n = []
        for x in words:
            d[x] = d.get(x,0) + 1
        s = sorted(d.items(), key = lambda x:(-x[1], x[0]))
        for i in range(k):
            n.append(s[i][0])
        return n