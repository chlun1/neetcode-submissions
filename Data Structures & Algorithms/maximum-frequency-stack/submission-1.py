from collections import defaultdict


class FreqStack:
    def __init__(self):
        self.counts = defaultdict(int)
        self.count2stack = defaultdict(list)
        self._max = 0

    def push(self, val: int) -> None:
        count = self.counts[val] + 1
        self.counts[val] = count
        self._max = max(self._max, count)
        self.count2stack[count].append(val)

    def pop(self) -> int:
        val = self.count2stack[self._max].pop()
        self.counts[val] -= 1
        
        if not self.count2stack[self._max]:
            self._max -= 1

        return val

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()