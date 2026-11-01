from collections import defaultdict


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        indices = defaultdict(list)

        for i, c in enumerate(s):
            if c in indices and len(indices[c]) == 2:
                indices[c][1] = i
            else:
                indices[c].append(i)
                
        res = 0

        for k, v in indices.items():
            if len(v) < 2:
                continue

            start, end = v
            mids = set()

            for i in range(start + 1, end):
                mids.add(s[i])

            res += len(mids)

        return res
