class Solution:
    def checkValidString(self, s: str) -> bool:
        open_count = 0
        for c in s:
            if c == '(' or c == '*':
                open_count += 1
            else:
                open_count -= 1
            if open_count < 0:
                return False
        
        close_count = 0
        for c in reversed(s):
            if c == ')' or c == '*':
                close_count += 1
            else:
                close_count -= 1
            if close_count < 0:
                return False
        
        return True