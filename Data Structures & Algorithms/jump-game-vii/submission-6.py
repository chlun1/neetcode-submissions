from collections import deque


class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == "1":
            return False
            
        farthest = 0
        q = deque([0])

        while q:
            i = q.popleft()
            start = max(i + minJump, farthest + 1)
            end = min(i + maxJump, len(s) - 1)

            for j in range(start, end + 1):
                if s[j] == "0":
                    q.append(j)
                    if j == len(s) - 1:
                        return True

            farthest = end
            
        return False
            