class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(start, subset, total):
            if total > target:
                return
            if total == target:
                res.append(subset.copy())
                return

            for i in range(start, len(candidates)):
                num = candidates[i]
                if i > start and num == candidates[i - 1]:
                    continue
                subset.append(num)
                backtrack(i + 1, subset, total + num)
                subset.pop()

        backtrack(0, [], 0)

        return res
        