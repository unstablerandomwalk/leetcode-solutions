class Solution:
    def reverseWords(self, s: str) -> str:
        a = s.split()
        print(a)
        a = a[::-1]
        return " ".join(a)