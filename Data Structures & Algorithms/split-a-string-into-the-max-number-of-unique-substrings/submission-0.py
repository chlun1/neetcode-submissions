class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        res = 0

        def backtrack(i, substrings):
            nonlocal res
            if i == len(s):
                res = max(res, len(substrings))
                return

            for j in range(i, len(s)):
                sub = s[i: j + 1]
                if sub not in substrings:
                    substrings.add(sub)
                    backtrack(j + 1, substrings)
                    substrings.remove(sub)

        backtrack(0, set())

        return res
