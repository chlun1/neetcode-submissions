from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0
        cur_sum = 0
        comp = defaultdict(int)
        comp[cur_sum] += 1

        for i in range(1, n + 1):
            cur_sum = cur_sum + nums[i - 1]
            if comp[cur_sum - k] > 0:
                res += comp[cur_sum - k]
            comp[cur_sum] += 1

        return res
