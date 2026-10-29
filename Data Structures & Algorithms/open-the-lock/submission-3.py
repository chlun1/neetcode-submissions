from collections import deque


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        if "0000" == target:
            return 0

        q = deque([[0, 0, 0, 0]])
        t = [int(x) for x in target]
        turns = 0
        visited = set()
        for deadend in deadends:
            visited.add(tuple(int(x) for x in deadend))

        while q:
            turns += 1
            for _ in range(len(q)):
                curr = q.popleft()

                for pos in range(4):
                    for inc in [1, -1]:
                        curr_copy = curr.copy()
                        curr_copy[pos] += inc
                        curr_copy[pos] %= 10
                        if curr_copy == t:
                            return turns

                        key = tuple(curr_copy)
                        if (
                            0 <= curr_copy[pos] <= 9
                            and key not in visited
                        ):
                            q.append(curr_copy)
                            visited.add(key)

        return -1
        