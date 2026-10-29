class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(curr, options):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return

            for i in range(len(options)):
                curr.append(options[i])
                backtrack(curr, options[:i] + options[i + 1:])
                curr.pop()

        backtrack([], nums)

        return res
        