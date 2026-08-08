class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = sorted(Counter(word).values(), reverse=True)
        total = 0
        for i, f in enumerate(freq):
            presses = (i // 8) + 1
            total += f * presses
        return total