class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        h = {}
        m = set()
        for i in range(len(s)):
            if s[i] not in h:
                if t[i] in m:
                    return False
                h[s[i]] = t[i]
                m.add(t[i])
            else:
                if h[s[i]] != t[i]:
                    return False
        return True