class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        picked = [False] * len(nums)

        def backtrack(curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return

            for i in range(len(nums)):
                if not picked[i]:
                    curr.append(nums[i])
                    picked[i] = True
                    backtrack(curr)
                    curr.pop()
                    picked[i] = False

        backtrack([])

        return res
        