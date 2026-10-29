from collections import defaultdict

class FreqStack:

    def __init__(self):
        self.counts = defaultdict(int)
        self.count2stack = []

    def push(self, val: int) -> None:
        count = self.counts[val] + 1
        self.counts[val] = count
        if count > len(self.count2stack):
            self.count2stack.append([])

        self.count2stack[count - 1].append(val)

    def pop(self) -> int:
        val = self.count2stack[-1].pop()
        self.counts[val] -= 1
        if not self.count2stack[-1]:
            self.count2stack.pop()

        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()