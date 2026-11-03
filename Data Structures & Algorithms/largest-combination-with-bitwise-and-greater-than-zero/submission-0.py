class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        res = 0

        for i in range(32):
            count = 0
            for x in candidates:
                if x & (1 << i):
                    count += 1

            res = max(res, count)

        return res
