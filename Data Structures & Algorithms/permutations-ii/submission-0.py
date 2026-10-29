from collections import Counter


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        counts = Counter(nums)

        def backtrack(curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return

            for num in counts:
                if counts[num] > 0:
                    curr.append(num)
                    counts[num] -= 1
                    backtrack(curr)
                    curr.pop()
                    counts[num] += 1

        backtrack([])

        return res
        