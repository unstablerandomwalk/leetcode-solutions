class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        t = '#' + '#'.join(s) + '#'
        n = len(t)
        radius = [0] * n
        C = R = 0                      # center and right edge of current best

        for i in range(n):
            if i < R:
                mirror = 2 * C - i
                radius[i] = min(R - i, radius[mirror])   # free head start

            # expand past whatever we got for free
            while (i + radius[i] + 1 < n
                   and i - radius[i] - 1 >= 0
                   and t[i + radius[i] + 1] == t[i - radius[i] - 1]):
                radius[i] += 1

            if i + radius[i] > R:      # new rightmost reach → update
                C, R = i, i + radius[i]

        k = radius.index(max(radius))  # center of the longest
        best = max(radius)
        start = (k - best) // 2        # map back to original string
        return s[start : start + best]