from collections import deque


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set()
        q = deque([[0, 0, 0, 0]])
        t = [int(x) for x in target]
        turns = 0
        deadends_set = set()
        for deadend in deadends:
            deadends_set.add(tuple(int(x) for x in deadend))

        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                if tuple(curr) in deadends_set:
                    continue
                if curr == t:
                    return turns

                for pos in range(4):
                    for inc in [1, -1]:
                        curr_copy = curr.copy()
                        curr_copy[pos] += inc
                        curr_copy[pos] %= 10
                        key = tuple(curr_copy)
                        if (
                            0 <= curr_copy[pos] <= 9
                            and key not in visited
                        ):
                            q.append(curr_copy)
                            visited.add(key)

            turns += 1

        return -1
        