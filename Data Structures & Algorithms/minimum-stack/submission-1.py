class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        top = self.min_stack[-1] if self.min_stack else val
        self.stack.append(val)
        self.min_stack.append(min(val, top))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        print(self.stack)
        print(self.min_stack)
        return self.min_stack[-1]
