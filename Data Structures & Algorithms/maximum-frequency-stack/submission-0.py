from collections import defaultdict


class FreqStack:
    def __init__(self):
        self.counts = defaultdict(int)
        self.stack = []

    def push(self, val: int) -> None:
        self.counts[val] += 1
        self.stack.append(val)

    def pop(self) -> int:
        max_freq = max(self.counts.values())
        most_freq = set(
            v for v, count in self.counts.items()
            if count == max_freq
        )

        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i] in most_freq:
                res = self.stack[i]
                self.stack.pop(i)
                self.counts[res] -= 1
                return res

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()