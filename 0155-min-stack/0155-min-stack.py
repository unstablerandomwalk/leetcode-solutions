class MinStack:

    def __init__(self):
        self.stack=[]
        self.minstack=[]
    def push(self, value: int) -> None:
        self.stack.append(value)
        self.minstack.append(value)
        self.minstack.sort(reverse=True)
    def pop(self) -> None:
        x = self.stack.pop(-1)
        self.minstack.remove(x)
    def top(self) -> int:
        return self.stack[-1]
    def getMin(self) -> int:
        return self.minstack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()