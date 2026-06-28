class Solution:
    def lengthOfLastWord(self, s:str):
        x = s.strip()
        y = s.split()
        length = len(y[len(y)-1])
        return length
        