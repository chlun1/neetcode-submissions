from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pre = [0] * (n + 1)

        for i in range(1, n + 1):
            pre[i] = pre[i - 1] + nums[i - 1]

        res = 0
        comp = defaultdict(int)

        for l in range(n + 1):
            if comp[pre[l] - k] > 0:
                res += comp[pre[l] - k]
            comp[pre[l]] += 1

        return res
