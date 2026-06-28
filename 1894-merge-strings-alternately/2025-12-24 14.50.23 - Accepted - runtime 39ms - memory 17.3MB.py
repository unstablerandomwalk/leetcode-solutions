class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        k=0
        merged=[]
        while k<len(word1) or k<len(word2):
            if k<len(word1):
                merged.append(word1[k])
            if k<len(word2):
                merged.append(word2[k])
            k=k+1
        return "".join(merged)