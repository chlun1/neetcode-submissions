class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        intervals = {}

        for i, c in enumerate(s):
            if c not in intervals:
                intervals[c] = [i, i]
            else:
                intervals[c][1] = i

        res = []
        prev = [-1, -1]

        for intv in intervals.values():
            if prev[1] >= intv[0]:
                prev[1] = max(prev[1], intv[1])
            else:
                if prev[0] > -1:
                    res.append(prev[1] - prev[0] + 1)
                prev = intv

        res.append(prev[1] - prev[0] + 1)

        return res
        