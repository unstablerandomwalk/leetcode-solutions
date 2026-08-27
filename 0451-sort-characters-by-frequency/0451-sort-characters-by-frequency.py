class Solution:
    def frequencySort(self, s: str) -> str:
        h = {}
        for i in s:
            if i not in h:
                h[i] = 1
            else:
                h[i]+=1
        d = sorted(h.items(), key=lambda item: item[1], reverse = True)
        a = ""
        for i in d:
            a += i[0] * i[1]
        return a