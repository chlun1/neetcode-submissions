from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rq, dq = deque(), deque()
        
        for i, c in enumerate(senate):
            if c == "R":
                rq.append(i)
            else:
                dq.append(i)

        while rq and dq:
            ri = rq.popleft()
            di = dq.popleft()

            if ri < di:
                rq.append(ri + len(senate))
            else:
                dq.append(di + len(senate))

        return "Radiant" if rq else "Dire"
        