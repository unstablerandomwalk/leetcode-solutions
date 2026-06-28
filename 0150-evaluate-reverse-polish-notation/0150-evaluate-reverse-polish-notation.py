class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i in ("+-*/"):
                x = int(stack.pop(-1))
                y = int(stack.pop(-1))
                if i == "+":
                    res = x+y
                elif i == "*":
                    res = x*y
                elif i == "-":
                    res = y - x
                else:
                    res = int(y / x)
                stack.append(res)
            else:
                stack.append(i)
        return int(stack[0])