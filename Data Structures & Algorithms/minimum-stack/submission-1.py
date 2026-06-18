class MinStack:
    # O(1) -> time complexity | O(n) -> space complexity
    
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        mv = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(mv)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
