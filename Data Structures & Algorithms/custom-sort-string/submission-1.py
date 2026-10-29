from collections import Counter


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counts = Counter(s)
        res = []

        for c in order:
            while counts[c] > 0:
                counts[c] -= 1
                res.append(c)

        for c in counts.keys():
            while counts[c] > 0:
                counts[c] -= 1
                res.append(c)

        return "".join(res)
        