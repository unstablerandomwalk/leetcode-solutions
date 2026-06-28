class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in "([{":
                stack.append(i)
            else:
                if not stack:
                    return False
                if stack[-1] == "(" and i == ")":
                    stack.pop(-1)
                elif stack[-1] == "{" and i == "}":
                    stack.pop(-1)
                elif stack[-1] == "[" and i == "]":
                    stack.pop(-1)
                else:
                    return False
        if stack:
            return False
        else:
            return True