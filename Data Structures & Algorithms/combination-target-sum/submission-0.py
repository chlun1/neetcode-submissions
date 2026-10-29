class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(start, curr, total):
            if total == target:
                res.append(curr.copy())
            if total > target:
                return

            for i in range(start, len(nums)):
                num = nums[i]
                curr.append(num)
                backtrack(i, curr, total + num)
                curr.pop()

        backtrack(0, [], 0)

        return res
        