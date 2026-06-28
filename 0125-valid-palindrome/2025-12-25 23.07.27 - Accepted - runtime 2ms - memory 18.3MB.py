class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        result="".join(ch for ch in s if ch.isalnum())
        if result == result[::-1]:
            return True
        return False
