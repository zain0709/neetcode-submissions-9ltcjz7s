class MinStack:

    def __init__(self):
        self.stack = []
        self.stackMin = []
    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(self.stack)
    def pop(self) -> None:
        
        self.stack.pop()


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)
